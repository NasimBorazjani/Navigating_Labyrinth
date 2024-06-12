
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start))
    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves
        for i, tube in enumerate(state):
            if not tube:
                continue
            for j, target in enumerate(state):
                if i == j or len(target) == 9:
                    continue
                new_state = list(map(list, state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Red', 'Green', 'Blue', 'Blue', 'Green', 'Blue'], ['Red', 'Green', 'Green', 'Blue', 'Green', 'Blue'], ['Red', 'Red', 'Blue', 'Red', 'Green', 'Red']]
print(sort_it(tubes))
