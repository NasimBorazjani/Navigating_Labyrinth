
from collections import deque

jugs = [39, 110, 41, 54, 47, 33, 136, 40, 100]
buckets = [192, 459, 473, 493]
actions = []

def bfs():
    queue = deque([([0]*4, [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if state == buckets:
            return action
        for i in range(9):
            for j in range(4):
                if state[j] + jugs[i] <= buckets[j] and (j == 0 or state[j] + jugs[i] <= state[j-1]):
                    new_state = state[:]
                    new_state[j] += jugs[i]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, action + [('+', i+1, j+1)]))
                        visited.add(tuple(new_state))
                if state[j] > 0:
                    new_state = state[:]
                    new_state[j] = 0
                    if tuple(new_state) not in visited:
                        queue.append((new_state, action + [('-', i+1, j+1)]))
                        visited.add(tuple(new_state))
    return []

actions = bfs()
print(actions)
