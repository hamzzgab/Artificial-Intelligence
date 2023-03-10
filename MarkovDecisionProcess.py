import random


class MarkovDecisionProcess:
    def __init__(self, m=None, goal=None, isDeterministic=True):
        self.m = m
        self.goal = goal
        self.actions = {}

        self._discount = 0.8

        self.isDeterministic = isDeterministic
        self.create_actions()

        self.target = [self.goal]

    def set_heuristics(self):
        for key, value in self.actions.items():
            for k, v in value.items():
                # NON DETERMINISTIC
                if k == 'N':
                    value[k] = 0.8
                elif k == 'W':
                    value[k] = 0.1
                elif k == 'E':
                    value[k] = 0.5
                elif k == 'S':
                    value[k] = 0.5

    def create_actions(self):

        # DETERMINISTIC
        for key, val in self.m.maze_map.items():
            self.actions[key] = dict([(k, v) for k, v in val.items() if v == 1])

        # CHANGE TO STOCHASTIC
        if not self.isDeterministic:
            self.set_heuristics()

    def calculate_ValueIterationUtility(self, prob, reward, stateNext, utility):
        return prob * (reward + self._discount * utility[stateNext])

    def calculate_PolicyIterationUtility(self, prob, reward, state, stateNext, utility):
        return reward[state] + self._discount * (prob * utility[stateNext])

    def move(self, currentNode, direction):
        if direction == 'E':
            return currentNode[0], currentNode[1] + 1
        elif direction == 'W':
            return currentNode[0], currentNode[1] - 1
        elif direction == 'N':
            return currentNode[0] - 1, currentNode[1]
        elif direction == 'S':
            return currentNode[0] + 1, currentNode[1]


class ValueIteration(MarkovDecisionProcess):
    def __init__(self, m=None, goal=None, isDeterministic=True):

        super().__init__(m, goal, isDeterministic)

        self._reward = -4  # LIVING REWARD
        self._max_error = 10 ** (-3)

        self.utilities = self.target = [self.goal]
        self.utilities = {state: 0 for state in self.actions.keys()}
        self.utilities[self.target[0]] = 1

        self.policy_values = {}
        self.tracePath = {}

        self.explored = []
        self.calculate_valueIteration()

    def get_maxDelta(self, delta, utilityMax, state):
        return max(delta, abs(utilityMax - self.utilities[state]))

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
                        reward = 1000
                    utility = 0
                    utility += super().calculate_ValueIterationUtility(prob, reward, stateNext, self.utilities)
                    if utility > utilityMax:
                        utilityMax = utility
                        actionMax = action
                delta = self.get_maxDelta(delta, utilityMax, state)

                self.utilities[state] = utilityMax
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

            for direction in 'SNEW':
                if self.m.maze_map[node][direction] and self.move(node, direction) not in self.explored:
                    node_direction = self.move(node, direction)
                    if node_direction == self.target[0]:
                        bestNode = node_direction
                        break
                    if bestNodeVal is None:
                        bestNode = node_direction
                        bestNodeVal = self.utilities[bestNode]
                    else:
                        tempNode = node_direction
                        if bestNodeVal < self.utilities[tempNode]:
                            bestNode = tempNode
                            bestNodeVal = self.utilities[tempNode]
            self.explored.append(node)
            self.tracePath[node] = bestNode
            node = bestNode
        return self.tracePath


class PolicyIteration(MarkovDecisionProcess):
    def __init__(self, m=None, goal=None, isDeterministic=True):

        super().__init__(m, goal, isDeterministic)

        self.theta = 0.001

        self.target = [self.goal]

        self.utilities = {state: 0 for state in self.actions.keys()}
        self.utilities[self.target[0]] = pow(10, 7)

        self.policy_values = {s: random.choice('N') for s in self.actions.keys()}

        self._reward = {state: -40 for state in self.actions.keys()}  # LIVING REWARD
        self._reward[self.target[0]] = pow(10, 8)

        self.tracePath = {}

        self.calculate_policyIteration()

    def calculate_policyIteration(self):
        isPolicyChanged = True
        while isPolicyChanged:
            isPolicyChanged = False
            isValueChanged = True

            while isValueChanged:
                delta = 0
                isValueChanged = False

                for state in self.actions.keys():
                    if state == self.target[0]:
                        continue

                    old_action = self.policy_values[state]
                    max_utility = float('-infinity')
                    max_action = None

                    for action, prob in self.actions[state].items():
                        for direction in action:
                            if self.m.maze_map[state][direction]:
                                next_state = self.move(state, direction)

                        reward = self._reward[state]
                        if next_state == self.target[0]:
                            reward = pow(10, 7)

                        utility = self._reward[state] + self._discount * (prob * self.utilities[next_state])

                        if utility > max_utility:
                            max_utility = utility
                            max_action = action

                        self.policy_values[state] = max_action
                        self.utilities[state] = max_utility

                        if self.policy_values[state] != max_action:
                            isPolicyChanged = True
                            self.policy_values[state] = max_action

    def create_searchPath(self, currNode):
        node = currNode

        while node != self.target[0]:
            test = self.move(node, self.policy_values[node])
            self.tracePath[node] = test
            node = test

        return self.tracePath
