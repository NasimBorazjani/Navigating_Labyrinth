
from collections import deque

jugs = [117, 128, 36, 129, 103, 53, 21, 119, 105, 26]
goal = (394, 425, 426)
actions = [(i, '+', j) for i in range(9) for j in range(3)] + [(i, '-', j) for i in range(9) for j in range(3)]

def apply_action(state, action):
    i, op, j = action
    state = list(state)
    if op == '+':
        if state[j] + jugs[i] <= goal[j] and (j == 2 or state[j] + jugs[i] <= state[j+1]):
            state[j] += jugs[i]
    else:
        if state[j] - jugs[i] >= 0 and (j == 0 or state[j] - jugs[i] >= state[j-1]):
            state[j] -= jugs[i]
    return tuple(state)

def bfs():
    queue = deque([((0, 0, 0), [])])
    visited = set([(0, 0, 0)])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for action in actions:
            new_state = apply_action(state, action)
            if new_state not in visited:
                queue.append((new_state, path + [action]))
                visited.add(new_state)
    return None

print(bfs())
