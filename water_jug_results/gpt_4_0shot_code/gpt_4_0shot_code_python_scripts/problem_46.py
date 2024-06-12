
from collections import deque

jugs = [20, 142, 147, 48, 29, 113, 17, 18, 112, 68]
buckets = [287, 423, 583]
actions = [(i, '+', j) for i in jugs for j in range(3)] + [(i, '-', j) for i in jugs for j in range(3)]

def is_valid(state):
    return all(state[i] <= state[i+1] for i in range(2))

def perform_action(state, action):
    jug, op, bucket = action
    new_state = list(state)
    if op == '+':
        new_state[bucket] += jug
    else:
        new_state[bucket] -= jug
    return new_state if is_valid(new_state) else None

def bfs():
    queue = deque([([0, 0, 0], [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            new_state = perform_action(state, action)
            if new_state is not None and tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))
                visited.add(tuple(new_state))

print(bfs())
