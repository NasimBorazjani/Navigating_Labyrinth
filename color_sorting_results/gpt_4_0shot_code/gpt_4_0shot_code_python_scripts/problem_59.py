
from collections import deque

def sort_it(tubes):
    start = tuple(tuple(colors) for colors in tubes)
    goal = tuple(sorted(colors) for colors in start)
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
                if i == j or len(state[j]) == 8:
                    continue
                new_state = list(list(colors) for colors in state)
                new_state[j] = list(new_state[j])
                new_state[j].append(new_state[i].pop())
                new_state[i] = tuple(new_state[i])
                new_state[j] = tuple(new_state[j])
                new_state = tuple(sorted(new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + [(i, j)]))

tubes = [['Blue', 'Red', 'Red', 'Blue', 'Red'], ['Green', 'Blue', 'Blue', 'Red', 'Green'], ['Blue', 'Green', 'Red', 'Green', 'Green']]
print(sort_it(tubes))
