
from collections import deque

jugs = [137, 147, 73, 131, 91, 94, 72, 31, 103, 78]
goal = [263, 298, 505]

def bfs():
    start = (0, 0, 0)
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, actions = queue.popleft()
        if state == tuple(goal):
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                if state[j] - jug >= 0 and all(state[j] - jug >= state[k] for k in range(j)):
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
    return None

print(bfs())
