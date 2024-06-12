
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = [deque(tube) for tube in tubes]
    goal = [deque(sorted(tube)) for tube in start]
    visited = set()
    stack = [(start, [])]
    while stack:
        tubes, moves = stack.pop()
        if tubes == goal:
            return moves
        for i, tube in enumerate(tubes):
            if tube:
                ball = tube[-1]
                for j, target in enumerate(tubes):
                    if i != j and (len(target) < 7 or target[-1] == ball):
                        new_tubes = deepcopy(tubes)
                        new_tubes[j].append(new_tubes[i].pop())
                        state = tuple(tuple(tube) for tube in new_tubes)
                        if state not in visited:
                            visited.add(state)
                            new_moves = moves + [(i, j)]
                            stack.append((new_tubes, new_moves))

tubes = [['Green', 'Red', 'Blue', 'Green'], ['Blue', 'Blue', 'Red', 'Blue'], ['Red', 'Red', 'Green', 'Green']]
print(sort_it(tubes))
