
from collections import deque

def sort_it(tubes):
    start = tuple(map(tuple, tubes))
    goal = tuple(sorted(start, key=lambda x: x[0] if x else ''))
    visited = {start}
    queue = deque([([start], [])])

    while queue:
        path, moves = queue.popleft()
        state = path[-1]

        if state == goal:
            return moves

        for i, tube in enumerate(state):
            if not tube:
                continue
            for j, target in enumerate(state):
                if i == j or len(target) == 6:
                    continue
                new_state = list(map(list, state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((path + [new_state], moves + [(i, j)]))

tubes = [['Blue', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red']]
print(sort_it(tubes))
