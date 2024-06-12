
from collections import deque

def sort_it(tubes):
    start = tuple(tuple(tube) for tube in tubes)
    goal = (tuple(sorted(tube)) for tube in start)
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
                if i == j or len(state[j]) == 8:
                    continue
                new_state = list(list(t) for t in state)
                new_state[j].append(new_state[i].pop())
                new_state = tuple(tuple(t) for t in new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))
    return None

tubes = [['Red', 'Blue', 'Blue', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
