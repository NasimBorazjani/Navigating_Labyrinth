
from collections import deque

def bfs(jugs, goal):
    start = [0, 0, 0, 0]
    queue = deque([start])
    visited = {tuple(start): []}
    
    while queue:
        state = queue.popleft()
        if state == goal:
            return visited[tuple(state)]
        for i, jug in enumerate(jugs):
            for j, bucket in enumerate(state):
                if state[j] < jug and (j == 0 or state[j-1] >= jug):
                    new_state = state.copy()
                    new_state[j] = jug
                    if tuple(new_state) not in visited:
                        queue.append(new_state)
                        visited[tuple(new_state)] = visited[tuple(state)] + [('+', jug, j+1)]
                if state[j] > 0:
                    new_state = state.copy()
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        queue.append(new_state)
                        visited[tuple(new_state)] = visited[tuple(state)] + [('-', jug, j+1)]
    return []

jugs = [123, 124, 133, 85, 74]
goal = [276, 277, 355, 425]
print(bfs(jugs, goal))
