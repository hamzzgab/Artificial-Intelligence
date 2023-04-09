from tictactoe import Board
from IPython.display import clear_output

from tqdm import tqdm

import pickle, math, logging, random
import numpy as np

ROWS, COLS = 6, 7

name = 'qlvsran'
logger = logging.getLogger(name)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{name}.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class Connect4(Board):
    def __init__(self, dimensions):
        super().__init__(dimensions, x_in_a_row=4)
        self.state_dict = dict()

    def possible_moves(self):
        possible_moves_list = []
        for move in super().possible_moves():
            if move[0] in possible_moves_list:
                continue
            else:
                possible_moves_list.append(move[0])
        return possible_moves_list

    def push(self, col):
        self.state_dict = dict()
        for move in super().possible_moves():
            self.state_dict[move[0]] = []
        for move in super().possible_moves():
            self.state_dict[move[0]].append(move[1])
        super().push((col, max(self.state_dict[col])))
        # print(self

    def copy(self):
        board = Connect4(self.dimensions)
        board.turn = self.turn
        board.board = self.board.copy()
        return board


class ConnectFourBoard:
    def __init__(self, p1, p2):
        self.board = Connect4(dimensions=(ROWS, COLS))
        self.board.x_in_a_row = 4
        self.p1 = p1
        self.p2 = p2
        self.isEnd = False
        self.boardHash = None

    def displayBoard(self):
        print('-' * 23)
        print(self.board)
        print('-' * 23)

    def getBoard(self):
        self.boardHash = str(self.board.board.flatten())
        return self.boardHash

    def getWinner(self):
        return self.board.result()

    def getPositions(self):
        return self.board.possible_moves()

    def getGameOver(self):
        if self.board.result() is not None:
            return True
        return

    def setReward(self):
        result = self.getWinner()
        if result == 1:
            self.p1.setReward(1)
            self.p1.setReward(0)
        if result == 2:
            self.p1.setReward(0)
            self.p1.setReward(1)
        else:
            self.p1.setReward(0.1)
            self.p1.setReward(0.5)

    def setMove(self, move):
        self.board.push(move)

    def reset(self):
        self.board = Connect4(dimensions=(ROWS, COLS))
        self.board.x_in_a_row = 4
        self.boardHash = None
        self.isEnd = False

    def train(self, iterations=100):
        for i in tqdm(range(iterations)):
            while not self.getGameOver():
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
        self.displayBoard()

        while not self.getGameOver():
            # PLAYER 1
            positions = self.getPositions()
            print(f"{self.p1.name}'s turn... ")
            move = self.p1.getMove(positions, self.board)
            self.setMove(move)
            clear_output()
            self.displayBoard()

            winStatus = self.getWinner()
            if winStatus is not None:
                if winStatus == 1:
                    print(self.p1.name, "Wins!")
                    logger.warning(f"{self.p1.name}")

                else:
                    print("Tie!")
                    logger.warning(f"tie")
                    self.reset()
                    break
            else:
                positions = self.getPositions()
                print(f"{self.p2.name}'s turn... ")
                move = self.p2.getMove(positions, self.board)
                self.setMove(move)
                clear_output()
                self.displayBoard()

                winStatus = self.getWinner()
                if winStatus is not None:
                    if winStatus == 2:
                        print(self.p2.name, "Wins!")
                        logger.warning(f"{self.p2.name}")

                    else:
                        print("Tie!")
                        logger.warning(f"tie")
                        self.reset()
                        break


class RandomPlayer:
    def __init__(self, name='random'):
        self.name = name

    def getMove(self, positions, board):
        return random.choice(board.possible_moves())


class HumanPlayer:
    def __init__(self, name='human'):
        self.name = name

    @staticmethod
    def getMove(self, positions, board):
        while True:
            col = int(input('Enter col: '))
            return col


class MinimaxPlayer:
    def __init__(self, name='minimax'):
        self.name = name

    def minimax(self, board, depth, alpha, beta, maximizing):
        result = board.result()

        if depth == 0 or (board.has_won(1) or board.has_won(2)):
            # if (board.has_won(1) or board.has_won(2)):
            if result == 1:
                return 1, None

            if result == 2:
                return -1, None

            elif result == 0:
                return 0, None
            return 0, None

        if maximizing:
            # logger.warning('in-maximizing')
            maxEval = -math.inf
            bestMove = None
            # print(best_move, 'Maxi-BestMove')
            moves = board.possible_moves()
            # print(moves)
            for move in moves:
                _tempBoard = board.copy()
                _tempBoard.x_in_a_row = 4
                _tempBoard.push(move)

                # logger.warning('in-maximizing-loop')
                reward = self.minimax(_tempBoard, depth - 1, alpha, beta, False)[0]
                if reward > maxEval:
                    maxEval = reward
                    bestMove = move
                alpha = max(alpha, maxEval)
                if alpha >= beta:
                    break
            return maxEval, bestMove

        elif not maximizing:
            # logger.warning('in-minimizing')
            minEval = math.inf
            bestMove = None
            moves = board.possible_moves()

            for move in moves:
                _tempBoard = board.copy()
                _tempBoard.x_in_a_row = 4
                _tempBoard.push(move)

                reward = self.minimax(_tempBoard, depth - 1, alpha, beta, True)[0]
                if reward < minEval:
                    minEval = reward
                    bestMove = move
                beta = min(beta, minEval)
                if alpha >= beta:
                    break
            return minEval, bestMove

    def getMove(self, positions, board):
        reward, move = self.minimax(board, 5, -math.inf, math.inf, board.turn == 1)
        return move


class QLearningPlayer:
    def __init__(self, name='q-agent', alpha=0.2, epsilon=0.4, gamma=0.9):
        self.name = name
        self.states = []
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Q_table = {}

    def getBoard(self, board):
        boardHash = str(board.board.flatten())
        return boardHash

    def getMove(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.epsilon:
            col = np.random.choice(current_board.possible_moves())
            action = col
        else:
            maxValue = -999
            for move in positions:
                _nextBoard = current_board.copy()
                _nextBoard.x_in_a_row = 4
                _nextBoard.push(move)
                _nextBoardState = self.getBoard(_nextBoard)
                value = 0 if self.Q_table.get(_nextBoardState) is None else self.Q_table.get(_nextBoardState)
                if value >= maxValue:
                    maxValue = value
                    action = move
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
