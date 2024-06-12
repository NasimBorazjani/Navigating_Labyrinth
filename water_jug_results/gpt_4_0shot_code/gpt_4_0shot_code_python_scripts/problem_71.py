
from collections import deque

def bfs():
    jugs = [141, 92, 12, 77, 49, 140]
    goal = [304, 333, 349, 413]
    visited = set()
    queue = deque([([0, 0, 0, 0], [])])

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= goal[j] and (j == 0 or state[j] + jug <= state[j - 1]):
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, actions + [('+', jug, j + 1)]))
                if state[j] - jug >= 0 and (j == 3 or state[j] - jug >= state[j + 1]):
                    new_state = state[:]
                    new_state[j] -= jug
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, actions + [('-', jug, j + 1)]))
    return "Cannot be solved"

print(bfs())
