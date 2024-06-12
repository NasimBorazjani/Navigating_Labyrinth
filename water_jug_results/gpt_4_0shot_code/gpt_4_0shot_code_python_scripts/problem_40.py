
from collections import deque

jugs = [62, 144, 80, 72, 100, 127, 18, 82, 42, 99]
buckets = [258, 310, 514]
actions = []

def bfs():
    queue = deque([((0, 0, 0), [])])
    visited = set([(0, 0, 0)])

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

                if state[j] > 0:
                    new_state = list(state)
                    new_state[j] = 0
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
                        visited.add(new_state)

    return "No solution found"

actions = bfs()
print(actions)
