
from collections import deque

jugs = [116, 16, 79, 75, 30, 87, 28, 96, 15, 134]
goal = (155, 208, 295)

def valid(state):
    return all(x <= y for x, y in zip(state, state[1:]))

def bfs():
    queue = deque([(0, 0, 0)])
    visited = {(0, 0, 0): []}
    while queue:
        state = queue.popleft()
        if state == goal:
            return visited[state]
        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= goal[j]:
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if valid(new_state) and new_state not in visited:
                        queue.append(new_state)
                        visited[new_state] = visited[state] + [('+', jug, j+1)]
                if state[j] - jug >= 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if valid(new_state) and new_state not in visited:
                        queue.append(new_state)
                        visited[new_state] = visited[state] + [('-', jug, j+1)]
    return []

print(bfs())
