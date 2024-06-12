
from collections import deque

jugs = [58, 18, 19, 47, 86, 75, 119, 34]
buckets = [234, 331, 343, 379]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    queue = deque([([], [0]*len(buckets))])
    visited = set()
    while queue:
        path, state = queue.popleft()
        if state == buckets:
            return path
        for i, j in actions:
            if state[j] < jugs[i] and (j == 0 or state[j-1] >= jugs[i]):
                new_state = state[:]
                new_state[j] += jugs[i]
                if tuple(new_state) not in visited:
                    queue.append((path + [('+', i+1, j+1)], new_state))
                    visited.add(tuple(new_state))
            if state[j] > 0:
                new_state = state[:]
                new_state[j] -= jugs[i]
                if tuple(new_state) not in visited:
                    queue.append((path + [('-', i+1, j+1)], new_state))
                    visited.add(tuple(new_state))

print(bfs())
