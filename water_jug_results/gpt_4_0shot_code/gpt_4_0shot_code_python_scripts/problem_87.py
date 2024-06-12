
from collections import deque

def bfs(jugs, buckets, goal):
    queue = deque([([], buckets)])
    visited = set()

    while queue:
        actions, state = queue.popleft()

        if state == goal:
            return actions

        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 4)):
                    new_state = state[:]
                    new_state[j] += jug
                    new_actions = actions + [('+', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_actions, new_state))
                        visited.add(tuple(new_state))

                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    new_actions = actions + [('-', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_actions, new_state))
                        visited.add(tuple(new_state))

    return "No solution exists"

jugs = [36, 95, 47, 149, 58, 96, 81, 148]
buckets = [0, 0, 0, 0]
goal = [252, 307, 412, 431]

print(bfs(jugs, buckets, goal))
