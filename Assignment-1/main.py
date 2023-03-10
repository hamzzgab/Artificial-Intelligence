from pyamaze import maze, COLOR, agent, textLabel
import SearchAlgorithms as Algo
from MarkovDecisionProcess import ValueIteration, PolicyIteration
import timeit
import Gui as gui

rows, cols = grid = (int(gui.rows), int(gui.cols))
goal_x, goal_y = GOAL = (int(gui.goal_x), int(gui.goal_y))


def get_time(function):
    return timeit.timeit(function, number=1000, globals=globals())


# -----------------MAZE----------------------
m = maze(rows=rows, cols=cols)
m.CreateMaze(x=goal_x, y=goal_y, pattern=None,
             theme=COLOR.light, loopPercent=100)
# saveMaze=True)
# loadMaze=f'SavedMazes/Algorithms/{gui.AlgoMaze}')

if gui.run_search_algos:
    # -----------------ALGO----------------------
    Algo.NODES = 'ESNW'

    dfsPath = None
    bfsPath = None
    aStarPath = None
    agents = [0, 0, 0]

    for idx, val in enumerate(gui.AlgoRun):
        # -----------------DFS-----------------------
        if idx == 0 and val:
            DFS = Algo.DFS(m=m, goal=GOAL)
            DFS.set_params()
            DFS.search_path()
            dfsPath = DFS.get_forward_path()

            d = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=True,
                      color=COLOR.yellow)

            agents[0] = d

            calcDFSTime = round(get_time(DFS.search_path) + get_time(DFS.get_forward_path), 4)

            totalDFSPath = textLabel(m, f'DFS Path', len(dfsPath) + 1)
            totalDFSSearchedPath = textLabel(m, f'DFS Searched Path', len(DFS.searchedPath) + 1)
            totalDFSTime = textLabel(m, f'DFS Time', calcDFSTime)

        # -----------------BFS-----------------------
        if idx == 1 and val:
            BFS = Algo.BFS(m=m, goal=GOAL)
            BFS.set_params()
            BFS.search_path()
            bfsPath = BFS.get_forward_path()

            b = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=True,
                      color=COLOR.red)

            agents[1] = b

            calcBFSTime = round(get_time(BFS.search_path) + get_time(BFS.get_forward_path), 4)

            totalBFSPath = textLabel(m, f'BFS Path', len(bfsPath) + 1)
            totalBFSSearchedPath = textLabel(m, f'BFS Searched Path', len(BFS.searchedPath) + 1)
            totalBFSTime = textLabel(m, f'BFS Time', calcBFSTime)

        # -----------------A*------------------------
        if idx == 2 and val:
            AStar = Algo.AStar(m=m, goal=GOAL)
            AStar.set_params()
            AStar.search_path()
            aStarPath = AStar.get_forward_path()

            a = agent(parentMaze=m,
                      x=None, y=None,
                      shape='square', footprints=True, filled=False,
                      color=COLOR.green)

            agents[2] = a

            calcAStarTime = round(get_time(AStar.search_path) + get_time(AStar.get_forward_path), 4)

            totalAStarPath = textLabel(m, f'A* Path', len(aStarPath) + 1)
            totalAStarSearchedPath = textLabel(m, f'A* Searched Path', len(AStar.searchedPath) + 1)
            totalAStarTime = textLabel(m, f'A* Time', calcAStarTime)

    tracingDict = {}
    for i, val in enumerate([dfsPath, bfsPath, aStarPath]):
        if val is not None:
            tracingDict[agents[i]] = val

    # ----------------TRACING--------------------
    m.tracePath(tracingDict,
                delay=100, kill=False,
                showMarked=True)
    m.run()

if gui.run_mdp_algo:
    # -----------------ALGO----------------------
    setDeterministic = True

    # -----------------AGENT---------------------
    agents = [0, 0]

    pathVI = None
    pathPI = None
    # -----------------PATH----------------------
    if gui.SetValueIteration:
        trackVI = ValueIteration(m, GOAL, isDeterministic=setDeterministic)
        trackVI.calculate_valueIteration()

        v = agent(m, shape='square', footprints=True, color=COLOR.red)

        agents[0] = v

        pathVI, timeVI = trackVI.create_searchPath((rows, cols))

        timeVI += get_time(trackVI.calculate_valueIteration)

        totalVIPath = textLabel(m, f'Value Iteration Path', len(pathVI) + 1)
        totalVITime = textLabel(m, f'Value Iteration Time', round(timeVI, 4))

    if gui.SetPolicyIteration:
        trackPI = PolicyIteration(m, GOAL, isDeterministic=setDeterministic)
        trackPI.calculate_policyIteration()

        p = agent(m, shape='square', filled=True, footprints=True, color=COLOR.blue)

        agents[1] = p

        pathPI, timePI = trackPI.create_searchPath((rows, cols))

        timePI += get_time(trackPI.calculate_policyIteration)

        totalPIPath = textLabel(m, f'Policy Iteration Path', len(pathPI) + 1)
        totalPITime = textLabel(m, f'Policy Iteration Time', round(timePI, 4))

    tracingDict = {}
    for i, val in enumerate([pathVI, pathPI]):
        if val is not None:
            tracingDict[agents[i]] = val

    # ----------------TRACING--------------------
    m.tracePath(tracingDict, delay=200)
    m.run()



