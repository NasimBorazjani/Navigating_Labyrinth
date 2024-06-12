
from collections import deque

def bfs(jugs, buckets, goal):
    queue = deque([([], buckets)])
    visited = set()

    while queue:
        actions, state = queue.popleft()

        if state == goal:
            return actions

        for i, jug in enumerate(jugs):
            for j, bucket in enumerate(state):
                if bucket + jug <= goal[j] and all(bucket + jug <= b for b in state[j+1:]):
                    new_state = state[:j] + [bucket + jug] + state[j+1:]
                    if tuple(new_state) not in visited:
                        queue.append((actions + [('+', i+1, j+1)], new_state))
                        visited.add(tuple(new_state))

                if bucket > 0:
                    new_state = state[:j] + [0] + state[j+1:]
                    if tuple(new_state) not in visited:
                        queue.append((actions + [('-', i+1, j+1)], new_state))
                        visited.add(tuple(new_state))

    return None

jugs = [51, 75, 112, 122, 54, 129, 31, 127, 113]
buckets = [0, 0, 0, 0]
goal = [338, 431, 493, 550]

actions = bfs(jugs, buckets, goal)
print(actions)
