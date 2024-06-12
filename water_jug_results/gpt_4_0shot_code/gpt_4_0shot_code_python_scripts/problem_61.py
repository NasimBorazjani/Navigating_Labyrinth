
from collections import deque

jugs = [56, 92, 66, 85, 65, 136]
buckets = [209, 293, 326, 379]
actions = []

def bfs():
    queue = deque([([0]*4, [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        if state == buckets:
            return action
        for i in range(len(jugs)):
            for j in range(len(state)):
                if state[j] + jugs[i] <= buckets[j] and (j == 0 or state[j] + jugs[i] <= state[j-1]):
                    new_state = state.copy()
                    new_state[j] += jugs[i]
                    queue.append((new_state, action + [('+', jugs[i], j+1)]))
                if state[j] - jugs[i] >= 0:
                    new_state = state.copy()
                    new_state[j] -= jugs[i]
                    queue.append((new_state, action + [('-', jugs[i], j+1)]))

actions = bfs()
print(actions)
