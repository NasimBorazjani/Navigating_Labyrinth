
from collections import deque

jugs = [150, 84, 29, 140, 98, 83, 32]
buckets = [243, 250, 446]
actions = [('+', x, y+1) for x in jugs for y in range(3)] + [('-', x, y+1) for x in jugs for y in range(3)]

def is_valid(state):
    return all(x <= y for x, y in zip(state, state[1:]))

def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] += action[1]
    else:
        new_state[action[2]-1] -= action[1]
    return new_state if is_valid(new_state) else None

def bfs():
    queue = deque([([0, 0, 0], [])])
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
            if new_state is not None:
                queue.append((new_state, path + [action]))

print(bfs())
