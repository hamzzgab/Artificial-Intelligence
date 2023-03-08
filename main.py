import SearchAlgo
from pyamaze import maze, COLOR, agent, textLabel
import timeit

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

GOAL = {'x': 1,
        'y': 1}

# -----------------MAZE----------------------
m = maze(rows=150, cols=150)
m.CreateMaze(x=GOAL['x'], y=GOAL['y'], pattern=None,
             theme=COLOR.light, loopPercent=100,
             saveMaze=False)

# -----------------ALGO----------------------
SearchAlgo.NODES = 'ESNW'

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
          shape='square', footprints=True, filled=True,
          color=COLOR.green)

# -----------------PATH----------------------
dfsPath = DFS.get_forward_path()
bfsPath = BFS.get_forward_path()
aStarPath = AStar.get_forward_path()

# | Marking cells that are visited
# m.markCells = list(set(dfsPath.values()).intersection(set(bfsPath.values())))

# -----------------TIMING--------------------
print(timeit.timeit(DFS.search_path, number=1000, globals=globals()))
print(timeit.timeit(BFS.search_path, number=1000, globals=globals()))
print(timeit.timeit(AStar.search_path, number=1000, globals=globals()))

# -----------------TEXT----------------------
totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
totalDFSSearchedPath = textLabel(m, f'DFS Path', len(DFS.searchedPath) + 1)

totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)
totalBFSSearchedPath = textLabel(m, f'BFS Searched Path', len(BFS.searchedPath) + 1)

totalAStarPath = textLabel(m, f'A* Path', len(aStarPath) + 1)
totalAStarSearchedPath = textLabel(m, f'A* Searched Path', len(AStar.searchedPath) + 1)

# ----------------TRACING--------------------
m.tracePath({
                d: dfsPath,
                b: bfsPath,
                a: aStarPath
            },
            delay=2, kill=False,
            showMarked=True)
m.run()
