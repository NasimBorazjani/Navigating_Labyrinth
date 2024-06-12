
from collections import deque

jugs = [91, 141, 56, 65, 89, 40, 39, 92]
buckets = [294, 375, 459, 466]
actions = []

def bfs():
    queue = deque([(buckets, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == [0]*4:
            return path
        for i in range(7):
            for j in range(4):
                if state[j] >= jugs[i] and (state[j]-jugs[i] >= state[j+1] if j < 3 else True):
                    new_state = state[:]
                    new_state[j] -= jugs[i]
                    action = ('-', i+1, j+1)
                    if tuple(new_state) not in visited:
                        queue.append((new_state, path + [action]))
                        visited.add(tuple(new_state))
                if state[j] + jugs[i] <= buckets[j] and (state[j]+jugs[i] <= state[j+1] if j < 3 else True):
                    new_state = state[:]
                    new_state[j] += jugs[i]
                    action = ('+', i+1, j+1)
                    if tuple(new_state) not in visited:
                        queue.append((new_state, path + [action]))
                        visited.add(tuple(new_state))

actions = bfs()
print(actions)
