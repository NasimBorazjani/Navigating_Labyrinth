
from collections import deque

def bfs():
    jugs = [21, 62, 98, 143, 61, 110, 140, 40]
    goal = (280, 338, 353)
    visited = set()
    queue = deque([((0, 0, 0), [])])

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
                        visited.add(new_state)
                        queue.append((new_state, actions + [('+', jug, j+1)]))

                if state[j] > 0:
                    new_state = list(state)
                    new_state[j] = 0
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('-', jug, j+1)]))

    return "No solution found"

print(bfs())
