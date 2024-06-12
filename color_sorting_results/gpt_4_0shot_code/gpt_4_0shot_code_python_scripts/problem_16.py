
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = [deque(tube) for tube in tubes]
    goal = sorted(deepcopy(start), key=lambda x: x[0])
    visited = set()
    stack = [(start, [])]
    while stack:
        state, moves = stack.pop()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if tube:
                for j, target in enumerate(state):
                    if i != j and (len(target) < 6 or target[-1] == tube[-1]):
                        new_state = deepcopy(state)
                        new_state[j].append(new_state[i].pop())
                        if str(new_state) not in visited:
                            visited.add(str(new_state))
                            new_moves = moves + [(i, j)]
                            stack.append((new_state, new_moves))

tubes = [['Red', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Red', 'Blue'], ['Blue', 'Red', 'Green', 'Blue']]
print(sort_it(tubes))
