
from collections import deque

def bfs(initial_state, goal_state, jugs):
    queue = deque([(initial_state, [])])
    visited = {tuple(initial_state): []}

    while queue:
        state, actions = queue.popleft()
        if state == goal_state:
            return actions
        for i, (jug, bucket) in enumerate(zip(jugs, state)):
            if state[i] < goal_state[i]:
                if state[i] + jug < goal_state[i]:
                    new_state = list(state)
                    new_state[i] += jug
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('+', jug, i+1)]))
                        visited[tuple(new_state)] = actions + [('+', jug, i+1)]
                else:
                    new_state = list(state)
                    new_state[i] = goal_state[i]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('-', jug, i+1)]))
                        visited[tuple(new_state)] = actions + [('-', jug, i+1)]
            elif state[i] > goal_state[i]:
                new_state = list(state)
                new_state[i] -= jug
                if tuple(new_state) not in visited:
                    queue.append((new_state, actions + [('-', jug, i+1)]))
                    visited[tuple(new_state)] = actions + [('-', jug, i+1)]

    return None

jugs = [36, 72, 16, 80, 45, 67, 38, 32, 149, 37]
initial_state = [0, 0, 0]
goal_state = [201, 202, 233]

actions = bfs(initial_state, goal_state, jugs)
print(actions)
