
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
                if state[j] + jug <= goal[j] and state[j] + jug <= (state[j+1] if j < 3 else float('inf')):
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

    return None

jugs = [59, 104, 79, 23, 20, 60, 14, 15, 119, 105]
buckets = [0, 0, 0, 0]
goal = [215, 403, 420, 504]

print(bfs(jugs, buckets, goal))
