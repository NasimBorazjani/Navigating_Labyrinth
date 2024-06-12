
from collections import deque

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
                new_state = list(map(list, state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Blue'], ['Red', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
