
from collections import deque

def bfs(start, target, jugs, actions):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for action in actions:
            next_state = perform_action(state, action, jugs)
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)
    return []

def perform_action(state, action, jugs):
    operation, jug, bucket = action
    state = list(state)
    if operation == '+':
        state[bucket-1] += jugs[jug-1]
    else:
        state[bucket-1] -= jugs[jug-1]
    return tuple(state)

jugs = [82, 91, 135, 11, 12, 19, 143, 60]
buckets = [231, 288, 342, 410]
actions = [('+', x+1, y+1) for x in range(len(jugs)) for y in range(len(buckets))] + \
           [('-', x+1, y+1) for x in range(len(jugs)) for y in range(len(buckets))]

start = (0, 0, 0, 0)
target = tuple(buckets)

path = bfs(start, target, jugs, actions)
print(path)
