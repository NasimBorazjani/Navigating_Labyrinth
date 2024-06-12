
from collections import deque

def bfs(start, target, jugs, actions):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for action in actions:
            next_state = action(state, jugs)
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)
    return []

def add(state, jugs):
    return tuple(min(state[i] + jugs[i], target[i]) for i in range(4))

def remove(state, jugs):
    return tuple(max(state[i] - jugs[i], 0) for i in range(4))

jugs = [34, 98, 27, 19, 52, 53]
start = (0, 0, 0, 0)
target = (257, 260, 269, 291)
actions = [add, remove]

path = bfs(start, target, jugs, actions)
for action in path:
    print(action.__name__, action(start, jugs))
