
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
                if state[j] + jug <= goal[j] and state[j] + jug <= (state[j+1] if j < 3 else float('inf')):
                    new_state = state[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('+', jug, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('-', jug, j+1)]))
                        visited.add(tuple(new_state))
    return "Cannot be solved"

jugs = [95, 111, 144, 57, 13, 58, 12]
goal = [226, 271, 331, 394]
print(bfs(jugs, goal))
