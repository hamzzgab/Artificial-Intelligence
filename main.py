from pyamaze import maze, COLOR, agent, textLabel
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

GOAL = {'x': 1,
        'y': 1}

# -----------------MAZE----------------------
m = maze(rows=25, cols=25)
m.CreateMaze(x=GOAL['x'], y=GOAL['y'], pattern=None,
             theme=COLOR.light, loopPercent=30,
             saveMaze=False)

# -----------------ALGO----------------------
SearchAlgo.NODES = 'ESNW'

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

# -----------------PATH----------------------

dfsPath = DFS.get_forward_path()
bfsPath = BFS.get_forward_path()

# | Marking cells that are visited
m.markCells = list(set(dfsPath.values()).intersection(set(bfsPath.values())))

# -----------------TEXT----------------------
# | Limitation [text is not dynamic]
totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)

# ----------------TRACING--------------------
# | Tracing the path to the goal
m.tracePath({
                d: dfsPath,
                b: bfsPath,
            },
            delay=2, kill=False,
            showMarked=True)
m.run()
