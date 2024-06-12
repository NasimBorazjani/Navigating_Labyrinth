
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
    next_state = list(state)
    if action[0] == '+':
        next_state[action[2]-1] += jugs[action[1]-1]
    else:
        next_state[action[2]-1] -= jugs[action[1]-1]
    return tuple(next_state)

jugs = [67, 98, 66, 59, 37, 61, 128, 92]
actions = [('+', i+1, j+1) for i in range(len(jugs)) for j in range(4)] + \
           [('-', i+1, j+1) for i in range(len(jugs)) for j in range(4)]
start = (0, 0, 0, 0)
target = (308, 309, 387, 433)

print(bfs(start, target, jugs, actions))
