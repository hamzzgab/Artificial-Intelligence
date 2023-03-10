from MarkovDecisionProcess import ValueIteration, PolicyIteration
from pyamaze import maze, agent, COLOR

rows, cols = (10, 10)
goal_x, goal_y = goal = (1, 1)

# -----------------MAZE----------------------
m = maze(rows, cols)
m.CreateMaze(goal_x, goal_y, loopPercent=100, theme=COLOR.light)

# -----------------ALGO----------------------
setDeterministic = True
trackVI = ValueIteration(m, goal, isDeterministic=setDeterministic)
trackPI = PolicyIteration(m, goal, isDeterministic=setDeterministic)

# -----------------AGENT---------------------
agent1 = agent(m, shape='arrow', footprints=True, color=COLOR.red)
agent2 = agent(m, shape='arrow', footprints=True, color=COLOR.blue)

# -----------------PATH----------------------
pathVI = trackVI.create_searchPath((rows, cols))
pathPI = trackPI.create_searchPath((rows, cols))

# ----------------TRACING--------------------
m.tracePath({agent1: pathVI, agent2: pathPI}, delay=200)
m.run()
