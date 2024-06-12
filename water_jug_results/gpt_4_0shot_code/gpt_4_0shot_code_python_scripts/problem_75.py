
from collections import deque

jugs = [98, 121, 131, 126, 141, 125, 20]
buckets = [309, 395, 407, 429]

def valid(state):
    return all(state[i] <= state[i+1] for i in range(len(state)-1))

def bfs():
    start = (tuple([0]*len(buckets)), [])
    queue = deque([start])
    visited = set([start[0]])

    while queue:
        state, actions = queue.popleft()
        if state == tuple(buckets):
            return actions
        for i, jug in enumerate(jugs):
            for j in range(len(buckets)):
                if state[j] + jug <= buckets[j]:
                    new_state = list(state)
                    new_state[j] += jug
                    if valid(new_state) and tuple(new_state) not in visited:
                        queue.append((tuple(new_state), actions + [('+', i+1, j+1)]))
                if state[j] - jug >= 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    if valid(new_state) and tuple(new_state) not in visited:
                        queue.append((tuple(new_state), actions + [('-', i+1, j+1)]))
                visited.add(tuple(new_state))
    return None

print(bfs())
