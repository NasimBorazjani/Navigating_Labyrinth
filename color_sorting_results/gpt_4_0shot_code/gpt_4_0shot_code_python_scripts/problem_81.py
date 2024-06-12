
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = [deque(tube) for tube in tubes]
    goal = [deque(sorted(tube)) for tube in tubes]
    visited = set()
    stack = [(start, [])]
    while stack:
        state, moves = stack.pop()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if tube:
                for j, target in enumerate(state):
                    if i != j and (len(target) < 9 or target[-1] == tube[-1]):
                        new_state = deepcopy(state)
                        new_state[j].append(new_state[i].pop())
                        new_moves = moves + [(i, j)]
                        tuple_state = tuple(tuple(tube) for tube in new_state)
                        if tuple_state not in visited:
                            visited.add(tuple_state)
                            stack.append((new_state, new_moves))

tubes = [['Green', 'Red', 'Red', 'Red', 'Green', 'Green'], ['Green', 'Red', 'Red', 'Blue', 'Red', 'Blue'], ['Blue', 'Blue', 'Blue', 'Green', 'Blue', 'Green']]
print(sort_it(tubes))
