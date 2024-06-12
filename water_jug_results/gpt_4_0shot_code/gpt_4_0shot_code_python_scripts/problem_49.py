
from collections import deque

def bfs():
    jugs = [22, 98, 38, 116, 140, 115, 21, 80, 92, 27]
    goal = (279, 488, 578)
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
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                if state[j] - jug >= 0 and all(state[j] - jug >= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
    return None

print(bfs())
