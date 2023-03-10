from queue import PriorityQueue
import time
NODES = 'ESNW'


def calculateManhattanDistance(x, y=(1, 1)):
    x1, y1 = x
    x2, y2 = y
    return abs(x1 - x2) + abs(y1 - y2)


class SearchAlgo:
    def __init__(self, m=None, goal=None, algo=None):

        self.m = m
        if goal is None:
            raise AssertionError("Goal Cannot be None")
        self.goal = goal
        self.algo = algo

        self.nodes = NODES

        # | DFS BFS PARAMETERS
        self.explored = []
        self.frontier = []

        # | A* PARAMETERS
        self.g_score = {}
        self.f_score = {}
        self.store = PriorityQueue()

        self.currCell = None
        self.start = (self.m.rows, self.m.cols)

        # | PATHS
        self.algoPath = {}
        self.searchedPath = [self.start]
        self.forward_path = {}
        self.forwardPathCell = self.goal

        self.i = 0

        # self.mainTime = 0

    def set_params(self):
        if self.algo in ['dfs', 'bfs']:
            self.explored = [self.start]
            self.frontier = [self.start]

        elif self.algo in 'a*':
            self.g_score = {cell: float('inf') for cell in self.m.grid}
            self.f_score = {cell: float('inf') for cell in self.m.grid}

            self.g_score[self.start] = 0
            self.f_score[self.start] = calculateManhattanDistance(self.start)

            self.store.put((self.f_score, self.f_score, self.start))

        else:
            raise AssertionError("Algorithm specified incorrectly")

    def set_searched_path(self, node):
        self.searchedPath.append(node)

    def get_stopping_condition(self):
        if self.algo in ['dfs', 'bfs']:
            return len(self.frontier) > 0
        elif self.algo == 'a*':
            return not self.store.empty()

    def get_current_cell(self):
        if self.algo == 'dfs':
            return self.frontier.pop()
        elif self.algo == 'bfs':
            return self.frontier.pop(0)
        elif self.algo == 'a*':
            return self.store.get()[2]

    def move(self, direction=None):
        if direction is None:
            raise AssertionError("Direction cannot be None")
        else:
            if direction == 'N':
                return self.currCell[0] - 1, self.currCell[1]
            elif direction == 'S':
                return self.currCell[0] + 1, self.currCell[1]
            elif direction == 'E':
                return self.currCell[0], self.currCell[1] + 1
            elif direction == 'W':
                return self.currCell[0], self.currCell[1] - 1

    def search_path(self):
        start = time.time()
        self.i = 0
        # self.searchedPath = [self.start]
        while self.get_stopping_condition():
            self.currCell = self.get_current_cell()

            if self.algo in ['dfs', 'a*']:
                self.i += 1
                self.set_searched_path(self.currCell)

            if self.currCell == self.goal:
                print(self.algo, self.i)
                break

            for d in self.nodes:
                if self.m.maze_map[self.currCell][d]:
                    if d == self.nodes[0]:
                        child = self.move(direction=self.nodes[0])
                    elif d == self.nodes[1]:
                        child = self.move(direction=self.nodes[1])
                    elif d == self.nodes[2]:
                        child = self.move(direction=self.nodes[2])
                    elif d == self.nodes[3]:
                        child = self.move(direction=self.nodes[3])

                    # self.algorithm_logic(child)

                    if self.algo in ['dfs', 'bfs']:
                        if child in self.explored:
                            continue
                        self.explored.append(child)
                        self.frontier.append(child)
                        self.algoPath[child] = self.currCell

                    if self.algo == 'bfs':
                        self.i += 1
                        self.set_searched_path(child)

                    elif self.algo == 'a*':
                        temp_g_score = self.g_score[self.currCell] + 1
                        temp_f_score = temp_g_score + calculateManhattanDistance(child)

                        if temp_f_score < self.f_score[child]:
                            self.g_score[child] = temp_g_score
                            self.f_score[child] = temp_f_score
                            self.store.put((temp_f_score, calculateManhattanDistance(child), child))
                            self.algoPath[child] = self.currCell

        end = time.time()
        self.mainTime = end - start

    def get_forward_path(self):
        start = time.time()
        while self.forwardPathCell != self.start:
            self.forward_path[self.algoPath[self.forwardPathCell]] = self.forwardPathCell
            self.forwardPathCell = self.algoPath[self.forwardPathCell]
        end = time.time()

        self.mainTime = end - start
        return self.forward_path, self.i, self.mainTime


class DFS(SearchAlgo):
    def __init__(self, m, goal):
        super().__init__(m, goal, algo='dfs')


class BFS(SearchAlgo):
    def __init__(self, m, goal):
        super().__init__(m, goal, algo='bfs')


class AStar(SearchAlgo):
    def __init__(self, m, goal):
        super().__init__(m, goal, algo='a*')
