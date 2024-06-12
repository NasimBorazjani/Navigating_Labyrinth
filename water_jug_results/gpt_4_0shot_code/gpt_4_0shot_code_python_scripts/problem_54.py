
from collections import deque

jugs = [45, 67, 134, 133, 86, 66, 107, 94, 124, 122]
goal = [229, 303, 307]

def bfs():
    queue = deque([((0, 0, 0), [])])
    visited = set([(0, 0, 0)])

    while queue:
        state, actions = queue.popleft()

        if state == tuple(goal):
            return actions

        for i, x in enumerate(jugs):
            for j in range(3):
                if state[j] + x <= goal[j] and all(state[j] + x <= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] += x
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        queue.append((new_state, actions + [('+', x, j+1)]))
                        visited.add(new_state)

                if state[j] - x >= 0 and all(state[j] - x >= state[k] for k in range(j)):
                    new_state = list(state)
                    new_state[j] -= x
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        queue.append((new_state, actions + [('-', x, j+1)]))
                        visited.add(new_state)

    return None

print(bfs())
