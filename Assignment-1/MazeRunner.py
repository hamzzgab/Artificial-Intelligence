from pyamaze import maze, COLOR, agent, textLabel


class MazeRunner:
    def __init__(self, grid, goal, loopPercent=100, saveMaze=False, path=None, delay=100):
        self.rows, self.cols = grid
        self.goal_x, self.goal_y = goal['x'], goal['y']
        self.loopPercent = loopPercent
        self.saveMaze = saveMaze
        self.path = path
        self.delay = delay
        self.runner = None

        self.m = maze(rows=self.rows, cols=self.cols)

    def create_maze(self):
        self.m.CreateMaze(x=self.goal_x, y=self.goal_y,
                          pattern=None, theme=COLOR.light,
                          loopPercent=self.loopPercent,
                          saveMaze=self.saveMaze)

    def create_agent(self, shape='square', footprints=True, filled=True, color=COLOR.yellow):
        return agent(parentMaze=self.m, x=None, y=None, shape=shape,
                     footprints=footprints, filled=filled, color=color)

    def add_text(self, text, value):
        textLabel(self.m, text, value)

    def run(self):
        self.m.run()

    def trace_path(self, runner=None, path=None):
        self.m.tracePath({runner: path}, delay=self.delay)
        self.run()


MazeRunner = MazeRunner((5, 5), {'x': 1, 'y': 1}, loopPercent=100, saveMaze=False,
                        path={}, delay=100)
MazeRunner.create_maze()
runner = MazeRunner.create_agent(shape='square', footprints=True, filled=False)
MazeRunner.add_text(text='hello', value=3)
MazeRunner.trace_path(runner, path=[(3, 2), (2, 2)])
