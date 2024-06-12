
from collections import deque
from copy import deepcopy

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start))
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if not tube:
                continue
            for j in range(len(state)):
                if i == j or len(state[j]) == 7:
                    continue
                new_state = deepcopy(list(state))
                new_state[j] = list(new_state[j])
                new_state[j].append(new_state[i].pop())
                new_state[i] = tuple(new_state[i])
                new_state[j] = tuple(new_state[j])
                new_state = tuple(sorted(new_state))
                if new_state not in visited:
                    queue.append((new_state, moves + [(i, j)]))
                    visited.add(new_state)

tubes = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Red', 'Red', 'Green'], ['Blue', 'Blue', 'Green', 'Green']]
print(sort_it(tubes))
