
from collections import deque

jugs = [104, 14, 83, 46, 128, 34, 137, 15, 19, 126]
goal = (342, 373, 447)

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
                    if new_state not in visited:
                        queue.append(new_state)
                        visited[new_state] = visited[state] + [('+', i+1, j+1)]
                if state[j] - jug >= 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        queue.append(new_state)
                        visited[new_state] = visited[state] + [('-', i+1, j+1)]

print(bfs())
