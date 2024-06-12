
from collections import deque

jugs = [149, 128, 67, 43, 55, 38, 129]
buckets = [385, 387, 491]
actions = [('+', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))] + [('-', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))]

def is_valid(state):
    return all(state[i] <= state[i+1] for i in range(len(state)-1))

def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] += jugs[action[1]-1]
    else:
        new_state[action[2]-1] -= jugs[action[1]-1]
    return new_state if is_valid(new_state) else None

def bfs():
    queue = deque([([0]*len(buckets), [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        if state == buckets:
            return path
        for action in actions:
            new_state = apply_action(state, action)
            if new_state is not None and tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))

print(bfs())
