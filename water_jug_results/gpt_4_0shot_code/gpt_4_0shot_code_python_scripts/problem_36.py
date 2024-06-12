
from collections import deque

jugs = [15, 138, 24, 10, 30, 82, 11, 94]
buckets = [239, 275, 286]

def bfs():
    start = (0, 0, 0)
    visited = {start: []}
    queue = deque([start])

    while queue:
        state = queue.popleft()
        if state == tuple(buckets):
            return visited[state]

        for i, jug in enumerate(jugs):
            for j in range(3):
                if state[j] + jug <= buckets[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited[new_state] = visited[state] + [('+', i+1, j+1)]
                        queue.append(new_state)

                if state[j] > 0:
                    new_state = list(state)
                    new_state[j] = 0
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited[new_state] = visited[state] + [('-', i+1, j+1)]
                        queue.append(new_state)

print(bfs())
