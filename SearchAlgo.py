from queue import PriorityQueue

NODES = 'ESNW'


def calculateManhattanDistance(x, y=(1, 1)):
    x1, y1 = x
    x2, y2 = y
    return abs(x1 - y2) + abs(x2 - y2)


class SearchAlgo:
    def __init__(self, m=None, goal=None, algo=None):
        self.m = m
        if goal is None:
            raise AssertionError("Goal Cannot be None")
        if type(goal) != type({}):
            raise AssertionError(f"Goal of Incorrect Type:\n\tExpected: {type({})}\n\tGot: {type(goal)}")
        self.goal = goal
        self.algo = algo

        self.nodes = NODES

        self.start = (self.m.rows, self.m.cols)
        self.explored = []
        self.frontier = []
        self.currCell = None
        self.searchedPath = {}

        self.forward_path = {}
        self.cell = (goal['x'], goal['y'])

    def set_params(self):
        self.explored = [self.start]
        self.frontier = [self.start]

    def set_algorithm(self):
        if self.algo == 'dfs':
            return self.frontier.pop()
        elif self.algo == 'bfs':
            return self.frontier.pop(0)
        else:
            raise AssertionError("Algorithm Specified Incorrectly")

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
        while len(self.frontier) > 0:
            self.currCell = self.set_algorithm()
            if self.currCell == (self.goal['x'], self.goal['y']):
                break

            for d in self.nodes:
                if self.m.maze_map[self.currCell][d]:
                    """
                    self.nodes
                        E = 0
                        S = 1
                        N = 2
                        W = 3
                    """
                    if d == self.nodes[0]:
                        childCell = self.move(direction=self.nodes[0])
                    elif d == self.nodes[1]:
                        childCell = self.move(direction=self.nodes[1])
                    elif d == self.nodes[2]:
                        childCell = self.move(direction=self.nodes[2])
                    elif d == self.nodes[3]:
                        childCell = self.move(direction=self.nodes[3])

                    if childCell in self.explored:
                        continue
                    self.explored.append(childCell)
                    self.frontier.append(childCell)
                    self.searchedPath[childCell] = self.currCell

    def get_forward_path(self):
        while self.cell != self.start:
            self.forward_path[self.searchedPath[self.cell]] = self.cell
            self.cell = self.searchedPath[self.cell]
        return self.forward_path


class DFS(SearchAlgo):
    def __init__(self, m, goal):
        super().__init__(m, goal, algo='dfs')


class BFS(SearchAlgo):
    def __init__(self, m, goal):
        super().__init__(m, goal, algo='bfs')