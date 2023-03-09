from pyamaze import maze, agent, COLOR, textLabel


class MarkovDecisionProcess:
    def __init__(self, m=None, goal=None):
        self.m = m
        self.goal = goal

        self._reward = -1
        self._discount = 0.9
        self._max_error = 10 ** (-3)

        self.actions = {}

        self.create_actions()

        self.U = self.target = [self.goal]
        self.U = {state: 0 for state in self.actions.keys()}
        self.U[self.target[0]] = 1
        self.policy_values = {}
        self.tracePath = {}

        self.calculate_valueIteration()

        self.explored = []

    def create_actions(self):
        for key, val in self.m.maze_map.items():
            self.actions[key] = [(k, v) for k, v in val.items() if v == 1]

        for k, v in self.actions.items():
            self.actions[k] = dict(v)

        # SET HEURISTICS
        for key, val in self.actions.items():
            for k, v in val.items():
                # DETERMINISTIC
                if k == 'N':
                    val[k] = 1
                elif k == 'W':
                    val[k] = 1
                elif k == 'E':
                    val[k] = 1
                elif k == 'S':
                    val[k] = 1

    def move(self, currentNode, direction):
        if direction == 'E':
            return currentNode[0], currentNode[1] + 1
        elif direction == 'W':
            return currentNode[0], currentNode[1] - 1
        elif direction == 'N':
            return currentNode[0] - 1, currentNode[1]
        elif direction == 'S':
            return currentNode[0] + 1, currentNode[1]

    def calculate_valueIteration(self):
        while True:
            delta = 0
            for state in self.actions.keys():
                if state == self.target[0]:
                    continue
                utilityMax = float("-inf")
                actionMax = None
                for action, prob in self.actions[state].items():
                    for direction in action:
                        if self.m.maze_map[state][direction]:
                            stateNext = self.move(state, direction)
                    reward = self._reward
                    if stateNext == self.target[0]:
                        reward = 1
                    utility = 0
                    utility += prob * (reward + self._discount * self.U[stateNext])
                    if utility > utilityMax:
                        utilityMax = utility
                        actionMax = action
                delta = max(delta, abs(utilityMax - self.U[state]))

                self.U[state] = utilityMax
                self.policy_values[state] = actionMax

            if delta < self._max_error:
                break

    def create_searchPath(self, currNode):
        node = currNode

        while True:
            bestNode = None
            bestNodeVal = None
            if node == self.target[0]:
                break

            for direction in 'NWSE':
                if self.m.maze_map[node][direction] and self.move(node, direction) not in self.explored:
                    node_direction = self.move(node, direction)
                    if node_direction == self.target[0]:
                        bestNode = node_direction
                        # bestNodeVal = self.U[bestNode]
                        break
                    if bestNodeVal is None:
                        bestNode = node_direction
                        bestNodeVal = self.U[bestNode]
                    else:
                        tempNode = node_direction
                        if bestNodeVal < self.U[tempNode]:
                            bestNode = tempNode
                            bestNodeVal = self.U[tempNode]
            self.explored.append(node)
            self.tracePath[node] = bestNode
            node = bestNode
        return self.tracePath