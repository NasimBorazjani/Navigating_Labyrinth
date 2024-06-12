
from collections import deque

def bfs(buckets, jugs, goal):
    queue = deque([(buckets, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= goal[j] and state[j] + jug <= (state[j+1] if j < 3 else float('inf')):
                    new_state = state[:j] + [state[j] + jug] + state[j+1:]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('+', jug, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:j] + [0] + state[j+1:]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('-', jug, j+1)]))
                        visited.add(tuple(new_state))
    return "No solution exists"

buckets = [0, 0, 0, 0]
jugs = [56, 81, 132, 41, 86, 128, 57, 138]
goal = [232, 401, 444, 451]
print(bfs(buckets, jugs, goal))
