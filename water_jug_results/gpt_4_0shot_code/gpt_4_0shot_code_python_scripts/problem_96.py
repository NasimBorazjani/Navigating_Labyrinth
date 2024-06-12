
from collections import deque

jugs = [90, 21, 104, 111, 97, 22, 34, 15, 62, 52]
buckets = [177, 263, 294, 462]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    start = ([0]*len(buckets), [])
    queue = deque([start])
    visited = set([start[0]])

    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for i, j in actions:
            for sign in [1, -1]:
                new_state = state[:]
                new_state[j] += sign * jugs[i]
                if 0 <= new_state[j] <= buckets[j] and new_state == sorted(new_state):
                    action = ('+' if sign == 1 else '-', i+1, j+1)
                    if tuple(new_state) not in visited:
                        queue.append((new_state, path + [action]))
                        visited.add(tuple(new_state))
    return None

print(bfs())
