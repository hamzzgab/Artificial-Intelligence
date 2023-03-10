from MarkovDecisionProcess import ValueIteration, PolicyIteration
from pyamaze import maze, agent, COLOR, textLabel
import timeit

rows, cols = (10, 10)
goal_x, goal_y = goal = (1, 1)


def get_time(function):
    return timeit.timeit(function, number=1000, globals=globals())


# -----------------MAZE----------------------
m = maze(rows, cols)
m.CreateMaze(goal_x, goal_y, loopPercent=100, theme=COLOR.light)

# -----------------ALGO----------------------
setDeterministic = True
trackVI = ValueIteration(m, goal, isDeterministic=setDeterministic)
trackPI = PolicyIteration(m, goal, isDeterministic=setDeterministic)

trackVI.calculate_valueIteration()
trackPI.calculate_policyIteration()

print()

# -----------------AGENT---------------------
agent1 = agent(m, shape='square', footprints=True, color=COLOR.red)
agent2 = agent(m, shape='square', filled=True, footprints=True, color=COLOR.blue)

# -----------------PATH----------------------
pathVI, timeVI = trackVI.create_searchPath((rows, cols))
pathPI, timePI = trackPI.create_searchPath((rows, cols))

timeVI += get_time(trackVI.calculate_valueIteration)
timePI += get_time(trackPI.calculate_policyIteration)

totalVIPath = textLabel(m, f'Value Iteration Path', len(pathVI) + 1)
totalVITime = textLabel(m, f'Value Iteration Time', round(timeVI, 4))

totalPIPath = textLabel(m, f'Policy Iteration Path', len(pathPI) + 1)
totalPITime = textLabel(m, f'Policy Iteration Time', round(timePI, 4))

# ----------------TRACING--------------------
m.tracePath({
            agent1: pathVI,
            agent2: pathPI
            }, delay=200)
m.run()
