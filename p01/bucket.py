# opeardores:
# Op            Pre-condicoes            Efeitos
# Fill b1       X < 4 (evitar loops)     X = 4
# Fill b2       Y < 3                    Y = 3
# Empty b1      X > 0                    X = 0
# Empty b2      Y > 0                    Y = 0
# Pourb1b2FB2   X + Y >= 3 && Y < 3      X = X - (3 - Y) && Y = 3
# Pourb1b2Eb1   X + Y < 3 && X > 0       Y = Y + X && X = 0
# Pourb2b1FB1   X + Y >= 4 &&  X < 4     Y = Y - (4-X) && X = 4
# Pourb2b1EB2   X + Y < 4 && Y > 0       X = X + Y && Y = 0

import queue

from numpy import Infinity


class Node:
    def __init__(self, x, y, prev=None):
        self.x = x
        self.y = y
        self.prev = prev

    def __eq__(self, node):
        return self.get() == node.get()

    def get(self):
        return (self.x, self.y)

    def path(self):
        res = [self.get()]
        if (self.prev):
            res = self.prev.path() + res
        return res


def fill_b1(state):
    (x, y) = state

    if x < 4:
        return (4, y)


def fill_b2(state):
    (x, y) = state

    if y < 3:
        return (x, 3)


def empty_b1(state):
    (x, y) = state

    if x > 0:
        return (0, y)


def empty_b2(state):
    (x, y) = state

    if y > 0:
        return (x, 0)


def pour_b1_b2(state):
    (x, y) = state

    if x + y >= 3 and y < 3:
        return (x - (3-y), 3)
    elif x + y < 3 and x > 0:
        return (0, x + y)


def pour_b2_b1(state):
    (x, y) = state

    if x + y >= 4 and x < 4:
        return (4, y - (4-x))
    elif x + y < 3 and y > 0:
        return (x + y, 0)


def valid_solution(state):
    (x, _) = state
    return x == 2


operations = [fill_b1, fill_b2, empty_b1, empty_b2, pour_b1_b2, pour_b2_b1]
operations.reverse()


def bfs():
    visited = []

    q = queue.Queue()
    q.put(Node(0, 0))

    while not q.empty():
        curr_state = q.get()

        for op in operations:
            new_state = op(curr_state.get())

            if (new_state):
                (x, y) = new_state
                new_node = Node(x, y, curr_state)
                if (valid_solution(new_state)):
                    return new_node.path()
                if (new_node not in visited):
                    q.put(new_node)
                    visited.append(new_node)


def dfs_rec(visited, node):
    for op in operations:
        new_state = op(node.get())

        if (new_state):
            (x, y) = new_state
            new_node = Node(x, y, node)
            if (valid_solution(new_state)):
                return new_node.path()
            if (new_node not in visited):
                visited.append(new_node)
                value = dfs_rec(visited, new_node)
                if (value):
                    return value


def dfs():
    visited = []

    return dfs_rec(visited, Node(0, 0))


def its_rec(node, limit):
    if (limit == 0):
        return
    for op in operations:
        new_state = op(node.get())

        if (new_state):
            (x, y) = new_state
            new_node = Node(x, y, node)
            if (valid_solution(new_state)):
                return new_node.path()
            value = its_rec(new_node, limit - 1)
            if (value):
                return value


def its():
    limit = 1
    while 1:
        res = its_rec(Node(0, 0), limit)
        if (res):
            return res
        limit += 1


print(bfs())
print(dfs())
print(its())
