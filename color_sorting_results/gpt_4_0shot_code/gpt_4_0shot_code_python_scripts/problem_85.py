
from collections import deque

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
                if i == j or len(state[j]) == 9:
                    continue
                new_state = list(map(list, state))
                new_state[j].append(new_state[i].pop())
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Blue', 'Green', 'Red', 'Red', 'Blue', 'Red'], ['Green', 'Blue', 'Green', 'Blue', 'Red', 'Green'], ['Blue', 'Red', 'Green', 'Green', 'Blue', 'Red']]
print(sort_it(tubes))
