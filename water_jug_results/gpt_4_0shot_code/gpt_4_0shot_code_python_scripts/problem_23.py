
from collections import deque

def bfs():
    jugs = [118, 15, 88, 145, 84, 14, 107, 31]
    goal = [226, 258, 296]
    visited = set()
    queue = deque([[(0, 0, 0), []]])

    while queue:
        state, actions = queue.popleft()
        if state == tuple(goal):
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        queue.append([tuple(new_state), actions + [('+', i+1, j+1)]])
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    if tuple(new_state) not in visited:
                        queue.append([tuple(new_state), actions + [('-', i+1, j+1)]])
                        visited.add(tuple(new_state))
    return "No solution found"

print(bfs())
