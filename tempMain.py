from MarkovDecisionProcess import MarkovDecisionProcess
from pyamaze import maze, agent, COLOR

rows, cols = (5, 10)
goal_x, goal_y = goal = (1, 1)

# -----------------MAZE----------------------
m = maze(rows, cols)
m.CreateMaze(goal_x, goal_y, loopPercent=100, theme=COLOR.light,
             loadMaze='SavedMazes/MDP/maze-5x10.csv')

# -----------------ALGO----------------------
track = MarkovDecisionProcess(m, goal)

# -----------------AGENT---------------------
agent1 = agent(m, shape='arrow', footprints=True, color=COLOR.blue)

# -----------------PATH----------------------
path = track.create_searchPath((rows, cols))

# ----------------TRACING--------------------
m.tracePath({agent1: path}, delay=200)
m.run()
