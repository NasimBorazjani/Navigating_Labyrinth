
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start, key=lambda x: x[0] if x else ''))
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if not tube:
                continue
            for j in range(len(state)):
                if i == j or len(state[j]) == 6 or (state[j] and state[j][-1] != tube[-1]):
                    continue
                new_state = deepcopy(list(state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Green', 'Blue', 'Green', 'Red'], ['Red', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]
print(sort_it(tubes))
