from tictactoe import Board
from IPython.display import clear_output

from tqdm import tqdm

import pickle, math, logging, random
import numpy as np

ROWS, COLS = 3, 3

name = 'qlvsran'
logger = logging.getLogger(name)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{name}.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class TicTacToe:
    def __init__(self, p1, p2):
        self.board = Board(dimensions=(ROWS, COLS))
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        self.boardHash = None

    def getBoard(self):
        self.boardHash = str(self.board.board.flatten())
        return self.boardHash

    def getWinner(self):
        return self.board.result()

    def getPositions(self):
        return self.board.possible_moves()

    def setReward(self):
        result = self.getWinner()
        if result == 1:
            self.p1.setReward(1)
            self.p2.setReward(0)
        if result == 2:
            self.p1.setReward(1)
            self.p2.setReward(0)
        else:
            self.p1.setReward(0.1)
            self.p2.setReward(0.5)

    def reset(self):
        self.board = Board()
        self.boardHash = None
        self.isEnd = False

    def setMove(self, action):
        self.board.push(action)

    def train(self, rounds=100):
        for i in tqdm(range(rounds)):
            while not self.isEnd:
                positions = self.getPositions()
                p1_action = self.p1.getMove(positions, self.board)
                self.setMove(p1_action)
                board_hash = self.getBoard()
                self.p1.setState(board_hash)

                win = self.getWinner()
                if win is not None:
                    self.setReward()
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break

                else:
                    positions = self.getPositions()
                    p2_action = self.p2.getMove(positions, self.board)
                    self.setMove(p2_action)
                    board_hash = self.getBoard()
                    self.p2.setState(board_hash)

                    win = self.getWinner()
                    if win is not None:
                        self.setReward()
                        self.p1.reset()
                        self.p2.reset()
                        self.reset()
                        break

    def play(self):
        while not self.isEnd:
            positions = self.getPositions()
            print(f"{self.p1.name}'s turn...")
            p1_action = self.p1.getMove(positions, self.board)
            self.setMove(p1_action)
            clear_output()
            self.showBoard()

            win = self.getWinner()
            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")
                    logger.warning(f"{self.p1.name}")
                else:
                    print("tie!")
                    logger.warning(f"tie")
                self.reset()
                break

            else:
                positions = self.getPositions()
                print(f"{self.p2.name}'s turn...")
                p2_action = self.p2.getMove(positions, self.board)

                self.setMove(p2_action)
                clear_output()
                self.showBoard()

                win = self.getWinner()
                if win is not None:
                    if win == 2:
                        print(self.p2.name, "wins!")
                        logger.warning(f"{self.p2.name}")
                    else:
                        print("tie!")
                        logger.warning(f"tie")
                    self.reset()
                    break

    def showBoard(self):
        print('-' * 11)
        print(self.board)
        print('-' * 11)


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def getMove(positions, board):
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))

            move = (col, row)
            if move in positions:
                return move


class RandomPlayer:
    def __init__(self, name='random'):
        self.name = name

    def getMove(positions, board):
        randomMove = random.choice(board.possible_moves())
        return randomMove


class DefaultPlayer:
    def __init__(self, name='default'):
        self.name = name

    @staticmethod
    def getWinningMove(board, turn):
        for move in board.possible_moves():
            temp_board = board.copy()
            temp_board.push(tuple(move))
            if temp_board.result() == turn:
                return move
        return None

    @staticmethod
    def blockWinningMove(board, turn):
        opponent_turn = turn % 2 + 1
        for move in board.possible_moves():
            temp_board = board.copy()
            temp_board.set_mark(move.tolist(), opponent_turn)
            if temp_board.result() == opponent_turn:
                return move
        return None

    def getMove(self, positions, board):
        winMove = self.getWinningMove(board, board.turn)
        if winMove is not None:
            return winMove

        blockMove = self.blockWinningMove(board, board.turn)
        if blockMove is not None:
            return blockMove
        randomMove = random.choice(board.possible_moves())
        return randomMove


class MinimaxPlayer:
    def __init__(self, name='minimax'):
        self.name = name

    def minimax(self, board, alpha, beta, maximizing):
        case = board.result()

        if case == 1:
            return 1, None

        if case == 2:
            return -1, None

        elif case == 0:
            return 0, None

        if maximizing:
            maxEval = -100
            bestMove = None
            moves = board.possible_moves()

            for move in moves:
                _tempBoard = board.copy()
                _tempBoard.push(move)
                # logger.warning('max')
                eval = self.minimax(_tempBoard, alpha, beta, False)[0]
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
                alpha = max(alpha, maxEval)
                if alpha >= beta:
                    break
            return maxEval, bestMove

        elif not maximizing:
            minEval = 100
            bestMove = None
            moves = board.possible_moves()

            for move in moves:
                _tempBoard = board.copy()
                _tempBoard.push(move)
                # logger.warning('min')
                eval = self.minimax(_tempBoard, alpha, beta, True)[0]
                if eval < minEval:
                    minEval = eval
                    bestMove = move
                beta = min(beta, minEval)
                if alpha >= beta:
                    break
            return minEval, bestMove

    def getMove(self, positions, board):
        eval, move = self.minimax(board, -math.inf, math.inf, board.turn == 1)
        return move


class QLearningPlayer:
    def __init__(self, name='q-agent', alpha=0.2, epsilon=0.3, gamma=0.9):
        self.name = name
        self.states = []
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Q_table = {}

    def getHash(self, board):
        boardHash = str(board.board.flatten())
        return boardHash

    def getMove(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.epsilon:
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            maxValue = -999
            for p in positions:
                _nextBoard = current_board.copy()
                _nextBoard.push(tuple(p))
                _nextBoardState = self.getHash(_nextBoard)
                value = 0 if self.Q_table.get(_nextBoardState) is None else self.Q_table.get(_nextBoardState)
                if value >= maxValue:
                    maxValue = value
                    action = p
        return action

    def setState(self, state):
        self.states.append(state)

    def setReward(self, reward):
        for st in reversed(self.states):
            if self.Q_table.get(st) is None:
                self.Q_table[st] = 0
            self.Q_table[st] += self.alpha * (self.gamma * reward - self.Q_table[st])
            reward = self.Q_table[st]

    def reset(self):
        self.states = []

    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.Q_table, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.Q_table = pickle.load(fr)
        fr.close()
