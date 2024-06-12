
from collections import deque

def bfs():
    jugs = [99, 47, 122, 123, 72, 136, 51, 71]
    target = [274, 292, 361, 438]
    visited = set()
    queue = deque([([0, 0, 0, 0], [])])

    while queue:
        state, actions = queue.popleft()
        if state == target:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= target[j] and all(state[j] + jug <= state[k] for k in range(j+1, 4)):
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
    return []

print(bfs())
