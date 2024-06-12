
from collections import deque

jugs = [51, 129, 150, 138, 128, 72, 69, 111, 75]
buckets = [0, 0, 0]
goal = [454, 547, 601]

def bfs():
    queue = deque([(buckets, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
                        visited.add(tuple(new_state))
    return None

print(bfs())
