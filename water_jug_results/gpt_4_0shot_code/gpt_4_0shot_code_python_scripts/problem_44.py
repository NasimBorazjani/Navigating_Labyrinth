
from collections import deque

def bfs():
    jugs = [67, 55, 84, 148, 107, 114, 17, 143, 40, 39]
    goal = [192, 247, 479]
    visited = set()
    queue = deque([((0, 0, 0), [])])

    while queue:
        state, actions = queue.popleft()
        if state == tuple(goal):
            return actions
        for i, x in enumerate(jugs):
            for j in range(3):
                if state[j] + x <= goal[j] and all(state[j] + x <= state[k] for k in range(j + 1, 3)):
                    new_state = list(state)
                    new_state[j] += x
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('+', i + 1, j + 1)]))
                if state[j] - x >= 0 and all(state[j] - x >= state[k] for k in range(j)):
                    new_state = list(state)
                    new_state[j] -= x
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('-', i + 1, j + 1)]))
    return None

print(bfs())
