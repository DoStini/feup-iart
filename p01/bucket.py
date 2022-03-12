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
from search import Node, SearchSolution


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

solution = SearchSolution(valid_solution, operations)

print(solution.bfs((0, 0)))
print(solution.dfs((0, 0)))
print(solution.its((0, 0)))
