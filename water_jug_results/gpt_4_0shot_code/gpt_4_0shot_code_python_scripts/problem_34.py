
from collections import deque

jugs = [103, 109, 146, 101, 17, 145, 68]
buckets = [448, 466, 509]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    queue = deque([((0, 0, 0), [])])
    visited = set([(0, 0, 0)])

    while queue:
        state, path = queue.popleft()
        if state == tuple(buckets):
            return path
        for action in actions:
            i, j = action
            next_state = list(state)
            if next_state[j] + jugs[i] <= buckets[j] and (next_state[j] == 0 or next_state[j] >= next_state[j-1]):
                next_state[j] += jugs[i]
                if tuple(next_state) not in visited:
                    queue.append((tuple(next_state), path + [('+', i+1, j+1)]))
                    visited.add(tuple(next_state))
            if next_state[j] - jugs[i] >= 0 and (j == len(buckets)-1 or next_state[j] - jugs[i] <= next_state[j+1]):
                next_state[j] -= jugs[i]
                if tuple(next_state) not in visited:
                    queue.append((tuple(next_state), path + [('-', i+1, j+1)]))
                    visited.add(tuple(next_state))

print(bfs())
