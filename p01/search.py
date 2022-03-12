import queue


class Node:
    def __init__(self, state, prev=None):
        self.state = state
        self.prev = prev

    def __eq__(self, node):
        return self.get_state() == node.get_state()

    def get_state(self):
        return self.state

    def path(self):
        res = [self.state]
        if (self.prev):
            res = self.prev.path() + res
        return res


class SearchSolution:
    def __init__(self, valid_solution, operations):
        self.valid_solution = valid_solution
        self.operations = operations

    def bfs(self, initial_state):
        visited = []

        q = queue.Queue()
        q.put(Node(initial_state))

        while not q.empty():
            curr_state = q.get()

            for op in self.operations:
                new_state = op(curr_state.get_state())

                if (new_state):
                    new_node = Node(new_state, curr_state)
                    if (self.valid_solution(new_state)):
                        return new_node.path()
                    if (new_node not in visited):
                        q.put(new_node)
                        visited.append(new_node)

    def dfs_rec(self, visited, node):
        for op in self.operations:
            new_state = op(node.get_state())

            if (new_state):
                new_node = Node(new_state, node)
                if (self.valid_solution(new_state)):
                    return new_node.path()
                if (new_node not in visited):
                    visited.append(new_node)
                    value = self.dfs_rec(visited, new_node)
                    if (value):
                        return value

    def dfs(self, initial_state):
        visited = []

        return self.dfs_rec(visited, Node(initial_state))

    def its_rec(self, node, limit):
        if (limit == 0):
            return
        for op in self.operations:
            new_state = op(node.get_state())

            if (new_state):
                new_node = Node(new_state, node)
                if (self.valid_solution(new_state)):
                    return new_node.path()
                value = self.its_rec(new_node, limit - 1)
                if (value):
                    return value

    def its(self, initial_state):
        limit = 1
        while 1:
            res = self.its_rec(Node(initial_state), limit)
            if (res):
                return res
            limit += 1
