from pyamaze import maze, COLOR, agent

# -----------------MAZE----------------------
m = maze(rows=5, cols=5)
m.CreateMaze(x=1, y=1, pattern=None,
             theme=COLOR.light, loopPercent=100,
             saveMaze=False)

# -----------------AGENT---------------------
mdp = agent(parentMaze=m,
          x=None, y=None,
          shape='square', footprints=True, filled=True,
          color=COLOR.yellow)

mdpPath = [(5, 5), (4, 4)]
# ----------------TRACING--------------------
m.tracePath({
                mdp: mdpPath
            },
            delay=2, kill=False,
            showMarked=True)
m.run()