
from collections import deque

jugs = [19, 50, 12, 63, 143, 13]
buckets = [160, 170, 330]
actions = [('+', x, y) for x in jugs for y in range(3)] + [('-', x, y) for x in jugs for y in range(3)]

def is_valid(state):
    return all(x <= y for x, y in zip(state, state[1:]))

def bfs():
    queue = deque([([0, 0, 0], [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            new_state = state[:]
            if action[0] == '+':
                new_state[action[2]] += action[1]
            else:
                new_state[action[2]] -= action[1]
            if is_valid(new_state) and tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))
                visited.add(tuple(new_state))

print(bfs())
