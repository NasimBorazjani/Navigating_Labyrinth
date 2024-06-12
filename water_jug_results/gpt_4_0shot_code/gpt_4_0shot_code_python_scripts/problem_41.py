
from collections import deque

jugs = [80, 69, 12, 52, 107, 53, 82, 95, 108]
buckets = [170, 385, 499]
actions = []

def bfs():
    queue = deque([([0, 0, 0], [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if state == buckets:
            return action
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= buckets[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        queue.append((new_state, action + [('+', i+1, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        queue.append((new_state, action + [('-', i+1, j+1)]))
                        visited.add(tuple(new_state))
    return None

actions = bfs()
print(actions)
