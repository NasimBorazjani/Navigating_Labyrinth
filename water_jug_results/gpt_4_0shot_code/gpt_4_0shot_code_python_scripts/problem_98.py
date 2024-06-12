
from collections import deque

def bfs(jugs, goal):
    queue = deque([([0]*len(goal), [])])
    visited = set()
    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(len(goal)):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, len(goal))):
                    new_state = state[:]
                    new_state[j] += jug
                    new_actions = actions + [('+', jug, j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, new_actions))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    new_actions = actions + [('-', jug, j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, new_actions))
                        visited.add(tuple(new_state))
    return None

jugs = [137, 100, 82, 25, 21, 101, 118, 117, 26, 131]
goal = [272, 439, 458, 590]
print(bfs(jugs, goal))
