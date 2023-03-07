from pyamaze import maze, COLOR, agent, textLabel
from queue import PriorityQueue
import SearchAlgo

# ------------SEARCH ALGORITHM---------------
"""
# | _____PSEUDO_CODE_____
def SearchAlgo(m):
    # search algorithm
    return path

m = maze()
p = SearchAlgo(m)
a = agent(m)
m.tracePath({a: p})
m.run()
"""


def calculateManhattanDistance(x, y=(1, 1)):
    x1, y1 = x
    x2, y2 = y
    return abs(x1 - y2) + abs(x2 - y2)


def AStar(m):
    start = (m.rows, m.cols)

    # | INITIALIZE
    g_score = {cell: float('inf') for cell in m.grid}
    f_score = {cell: float('inf') for cell in m.grid}

    g_score[start] = 0
    f_score[start] = calculateManhattanDistance(start)

    # | CREATE QUEUE
    open = PriorityQueue()
    open.put((f_score, f_score, start))

    path = {}

    while not open.empty():
        currCell = open.get()[2]

        if currCell == (5, 19):
            break

        for d in 'WNES':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + calculateManhattanDistance(childCell)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, calculateManhattanDistance(childCell), childCell))
                    path[childCell] = currCell

    fwdPath={}
    cell=(5,19)
    while cell!=start:
        fwdPath[path[cell]]=cell
        cell=path[cell]
    return fwdPath


GOAL = {'x': 5,
        'y': 19}

# -----------------MAZE----------------------
m = maze(rows=25, cols=25)
m.CreateMaze(x=GOAL['x'], y=GOAL['y'], pattern=None,
             theme=COLOR.light, loopPercent=0,
             saveMaze=False)
# -----------------ALGO----------------------
path = AStar(m)

SearchAlgo.NODES = 'WNES'

DFS = SearchAlgo.DFS(m=m, goal=GOAL)
DFS.set_params()
DFS.search_path()

BFS = SearchAlgo.BFS(m=m, goal=GOAL)
BFS.set_params()
BFS.search_path()

# -----------------AGENT---------------------
d = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=True,
          color=COLOR.yellow)

b = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=False,
          color=COLOR.red)

a = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=True,
          color=COLOR.green)

# -----------------PATH----------------------

dfsPath = DFS.get_forward_path()
bfsPath = BFS.get_forward_path()

# -----------------TEXT----------------------
totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)
totalAStarPath = textLabel(m, f'A* Path', len(path) + 1)

# ----------------TRACING--------------------
# | Tracing the path to the goal
m.tracePath({
    a: path,
    # d: dfsPath,
    b: bfsPath
},
    delay=100, kill=False,
    showMarked=True)
m.run()
