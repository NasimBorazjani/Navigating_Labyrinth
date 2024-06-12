
from collections import deque

jugs = [137, 29, 70, 138, 47, 64, 87, 16]
goal = (295, 327, 442)

def bfs():
    queue = deque([((0, 0, 0), [])])
    visited = set([(0, 0, 0)])

    while queue:
        state, actions = queue.popleft()

        if state == goal:
            return actions

        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
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

    return None

actions = bfs()
if actions is None:
    print("No solution found.")
else:
    print(actions)
