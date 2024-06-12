
from collections import deque

jugs = [80, 76, 132, 60, 83, 28, 75, 26]
buckets = [337, 378, 398]

def bfs():
    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, actions = queue.popleft()
        if state == tuple(buckets):
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= buckets[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                        visited.add(new_state)
                if state[j] - jug >= 0 and all(state[k] - jug >= state[k-1] for k in range(j, 0, -1)):
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
                        visited.add(new_state)
    return None

print(bfs())
