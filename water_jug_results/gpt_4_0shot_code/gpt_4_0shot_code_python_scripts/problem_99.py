
from collections import deque

jugs = [32, 73, 55, 68, 61, 107, 44, 45, 74, 113]
buckets = [203, 429, 433, 477]
actions = [('+', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))] + [('-', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))]

def is_valid(state):
    for i in range(1, len(state)):
        if state[i] < state[i-1]:
            return False
    return True

def bfs():
    start = [0]*len(buckets)
    queue = deque([(start, [])])
    visited = set([tuple(start)])

    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            new_state = state[:]
            if action[0] == '+':
                new_state[action[2]-1] += jugs[action[1]-1]
            else:
                new_state[action[2]-1] -= jugs[action[1]-1]
            new_state[action[2]-1] = max(0, min(new_state[action[2]-1], buckets[action[2]-1]))
            if is_valid(new_state) and tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))
                visited.add(tuple(new_state))
    return None

print(bfs())
