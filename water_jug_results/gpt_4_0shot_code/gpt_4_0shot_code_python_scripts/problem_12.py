
from collections import deque

jugs = [46, 99, 145, 131, 78, 100]
target = [247, 340, 368]
buckets = [0, 0, 0]

def bfs():
    queue = deque([(buckets, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == target:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= target[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = state[:]
                    new_state[j] += jug
                    new_actions = actions + [('+', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, new_actions))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    new_actions = actions + [('-', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, new_actions))
    return None

print(bfs())
