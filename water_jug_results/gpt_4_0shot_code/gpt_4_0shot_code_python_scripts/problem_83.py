
from collections import deque

def bfs(jugs, goal):
    queue = deque([([0, 0, 0, 0], [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= goal[j]:
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited and all(new_state[k] <= new_state[k+1] for k in range(3)):
                        queue.append((new_state, actions + [('+', i+1, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] - jug >= 0:
                    new_state = state[:]
                    new_state[j] -= jug
                    if tuple(new_state) not in visited and all(new_state[k] <= new_state[k+1] for k in range(3)):
                        queue.append((new_state, actions + [('-', i+1, j+1)]))
                        visited.add(tuple(new_state))
    return "No solution exists"

jugs = [19, 42, 18, 127, 106, 32, 22, 137]
goal = [245, 252, 264, 314]
print(bfs(jugs, goal))
