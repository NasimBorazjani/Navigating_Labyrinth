
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
                for j, _ in enumerate(state):
                    if i != j and (len(state[j]) < 8 or state[j][-1] == tube[-1]):
                        new_state = deepcopy(state)
                        new_state[j].append(new_state[i].pop())
                        if str(new_state) not in visited:
                            visited.add(str(new_state))
                            new_moves = moves + [(i, j)]
                            stack.append((new_state, new_moves))

tubes = [['Green', 'Red', 'Green', 'Red', 'Green'], ['Blue', 'Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue', 'Blue']]
print(sort_it(tubes))
