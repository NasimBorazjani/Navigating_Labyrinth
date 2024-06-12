
from collections import deque

def bfs():
    jugs = [140, 58, 129, 130, 125]
    goal = (391, 401, 431)
    visited = {}
    queue = deque([((0, 0, 0), [])])

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, x in enumerate(jugs):
            if state[0] + x <= goal[0] and state[0] + x >= state[1] and state[0] + x >= state[2]:
                new_state = (state[0] + x, state[1], state[2])
                if new_state not in visited:
                    queue.append((new_state, actions + [('+', x, 1)]))
                    visited[new_state] = True
            if state[1] + x <= goal[1] and state[1] + x >= state[0] and state[1] + x >= state[2]:
                new_state = (state[0], state[1] + x, state[2])
                if new_state not in visited:
                    queue.append((new_state, actions + [('+', x, 2)]))
                    visited[new_state] = True
            if state[2] + x <= goal[2] and state[2] + x >= state[0] and state[2] + x >= state[1]:
                new_state = (state[0], state[1], state[2] + x)
                if new_state not in visited:
                    queue.append((new_state, actions + [('+', x, 3)]))
                    visited[new_state] = True
            if state[0] - x >= 0:
                new_state = (state[0] - x, state[1], state[2])
                if new_state not in visited:
                    queue.append((new_state, actions + [('-', x, 1)]))
                    visited[new_state] = True
            if state[1] - x >= 0:
                new_state = (state[0], state[1] - x, state[2])
                if new_state not in visited:
                    queue.append((new_state, actions + [('-', x, 2)]))
                    visited[new_state] = True
            if state[2] - x >= 0:
                new_state = (state[0], state[1], state[2] - x)
                if new_state not in visited:
                    queue.append((new_state, actions + [('-', x, 3)]))
                    visited[new_state] = True
    return []

print(bfs())
