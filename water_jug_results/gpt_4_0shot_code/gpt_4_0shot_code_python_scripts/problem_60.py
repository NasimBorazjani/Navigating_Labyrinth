
from collections import deque

def bfs(jugs, goal):
    visited = set()
    queue = deque([([0, 0, 0, 0], [])])

    while queue:
        state, actions = queue.popleft()

        if state == goal:
            return actions

        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= goal[j] and all(state[j] + jug <= state[k] for k in range(j+1, 4)):
                    new_state = state[:]
                    new_state[j] += jug
                    new_actions = actions + [('+', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, new_actions))

                if state[j] - jug >= 0 and all(state[j] - jug >= state[k] for k in range(j+1, 4)):
                    new_state = state[:]
                    new_state[j] -= jug
                    new_actions = actions + [('-', i+1, j+1)]
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, new_actions))

    return []

jugs = [78, 68, 49, 82, 77, 88]
goal = [176, 189, 251, 285]
print(bfs(jugs, goal))
