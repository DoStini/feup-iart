# estado (x1,y1, x2,y2)
# estado (M, C, M, C)
# inicial (0,0, 3,3)
# opeardores:
# Op            Pre-condicoes            Efeitos
# 2->1: 1 mis   x2 > y2 && x2 > 0        x1+1, y1, x2-1, y2
# 2->1: 2 mis   x2 > y2+1 && x2 > 1      x1+2, y1, x2-2, y2
# 2->1: 1 can   y2 > 0                   x1, y1+1, x2, y2-1
# 2->1: 2 can   y2 > 1                   x1, y1+2, x2, y2-2
# 2->1: 1-1     x2 > 1 && y2 > 1         x1-1, y1-1, x2+1, y2+1
# 1->2: 1 mis   x1 > y1 && x1 > 0        x1-1, y1, x2+1, y2
# 1->2: 2 mis   x1 > y1+1 x1 > 1         x1-2, y1, x2+2, y2
# 1->2: 1-1     x1 > 1 && y1 > 1         x1-1, y1-1, x2+1, y2+1
# 1->2: 1 can   y1 > 0                   x1, y1-1, x2, y2+1
# 1->2: 2 can   y1 > 1                   x1, y1-2, x2, y2+2

import queue
from search import Node, SearchSolution


def right_to_left_1_mis(state):
    (x1, y1, x2, y2) = state
    if (x2 > y2 and x2 > 0):
        return (x1+1, y1, x2-1, y2)


def right_to_left_2_mis(state):
    (x1, y1, x2, y2) = state
    if (x2 > y2+1 and x2 > 1):
        return (x1+2, y1, x2-2, y2)


def right_to_left_eq(state):
    (x1, y1, x2, y2) = state
    if (x2 > 1 and y2 > 1):
        return (x1+1, y1+1, x2-1, y2-1)


def left_to_right_1_mis(state):
    (x1, y1, x2, y2) = state
    if (x1 > y1 and x1 > 0):
        return (x1-1, y1, x2+1, y2)


def left_to_right_2_mis(state):
    (x1, y1, x2, y2) = state
    if (x1 > y1+1 and x1 > 1):
        return (x1-2, y1, x2+2, y2)


def left_to_right_1_can(state):
    (x1, y1, x2, y2) = state
    if (y1 > 0):
        return (x1, y1-1, x2, y2+1)


def left_to_right_2_can(state):
    (x1, y1, x2, y2) = state
    if (y1 > 1):
        return (x1, y1-2, x2, y2+2)


def left_to_right_eq(state):
    (x1, y1, x2, y2) = state
    if (x1 > 1 and y1 > 1):
        return (x1-1, y1-1, x2+1, y2+1)


def right_to_left_1_can(state):
    (x1, y1, x2, y2) = state
    if (y2 > 0):
        return (x1, y1+1, x2, y2-1)


def right_to_left_2_can(state):
    (x1, y1, x2, y2) = state
    if (y2 > 1):
        return (x1, y1+2, x2, y2-2)


def valid_solution(state):
    return (3, 3, 0, 0) == state


operations = [right_to_left_1_mis, right_to_left_2_mis, right_to_left_eq, right_to_left_1_can,  right_to_left_2_can,
              left_to_right_1_mis, left_to_right_2_mis, left_to_right_eq, left_to_right_1_can, left_to_right_2_can]

solution = SearchSolution(valid_solution, operations)

print(solution.bfs((0, 0, 3, 3)))
print(solution.dfs((0, 0, 3, 3)))
print(solution.its((0, 0, 3, 3)))
