import SearchAlgo
from pyamaze import maze, COLOR, agent, textLabel
import timeit
import gui


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

goal_x, goal_y = GOAL = (int(gui.goal_x), int(gui.goal_y))

# -----------------MAZE----------------------
m = maze(rows=int(gui.rows), cols=int(gui.cols))
m.CreateMaze(x=goal_x, y=goal_y, pattern=None,
             theme=COLOR.light, loopPercent=100,
             saveMaze=False)

# -----------------ALGO----------------------
SearchAlgo.NODES = 'SNWE'

DFS = SearchAlgo.DFS(m=m, goal=GOAL)
DFS.set_params()
DFS.search_path()

BFS = SearchAlgo.BFS(m=m, goal=GOAL)
BFS.set_params()
BFS.search_path()

AStar = SearchAlgo.AStar(m=m, goal=GOAL)
AStar.set_params()
AStar.search_path()

# -----------------AGENT---------------------
d = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=True,
          color=COLOR.yellow)

b = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=True,
          color=COLOR.red)

a = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=False,
          color=COLOR.green)

# -----------------PATH----------------------
dfsPath = DFS.get_forward_path()
bfsPath = BFS.get_forward_path()
aStarPath = AStar.get_forward_path()


# -----------------TIMING--------------------
def get_time(function):
    return timeit.timeit(function, number=1000, globals=globals())


calcDFSTime = round(get_time(DFS.search_path) + get_time(DFS.get_forward_path), 4)
calcBFSTime = round(get_time(BFS.search_path) + get_time(BFS.get_forward_path), 4)
calcAStarTime = round(get_time(AStar.search_path) + get_time(AStar.get_forward_path), 4)

# -----------------TEXT----------------------
totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
totalDFSSearchedPath = textLabel(m, f'DFS Searched Path', len(DFS.searchedPath) + 1)
totalDFSTime = textLabel(m, f'DFS Time', calcDFSTime)

totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)
totalBFSSearchedPath = textLabel(m, f'BFS Searched Path', len(BFS.searchedPath) + 1)
totalBFSTime = textLabel(m, f'BFS Time', calcBFSTime)

totalAStarPath = textLabel(m, f'A* Path', len(aStarPath) + 1)
totalAStarSearchedPath = textLabel(m, f'A* Searched Path', len(AStar.searchedPath) + 1)
totalAStarTime = textLabel(m, f'A* Time', calcAStarTime)

# ----------------TRACING--------------------
m.tracePath({
                d: dfsPath,
                b: bfsPath,
                a: aStarPath
            },
            delay=100, kill=False,
            showMarked=True)
m.run()


