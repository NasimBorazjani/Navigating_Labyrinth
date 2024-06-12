
from collections import deque

jugs = [127, 96, 108, 126, 132, 139, 146, 14]
buckets = [273, 349, 435, 503]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    start = [0]*len(buckets)
    queue = deque([(start, [])])
    visited = set([tuple(start)])
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for i, j in actions:
            if state[j] + jugs[i] <= buckets[j] and (j == len(buckets)-1 or state[j] + jugs[i] <= state[j+1]):
                new_state = state.copy()
                new_state[j] += jugs[i]
                if tuple(new_state) not in visited:
                    queue.append((new_state, path + [('+', i+1, j+1)]))
                    visited.add(tuple(new_state))
            if state[j] > 0:
                new_state = state.copy()
                new_state[j] = 0
                if tuple(new_state) not in visited:
                    queue.append((new_state, path + [('-', i+1, j+1)]))
                    visited.add(tuple(new_state))
    return None

print(bfs())
