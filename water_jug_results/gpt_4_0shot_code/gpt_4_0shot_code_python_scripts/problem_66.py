
from collections import deque

def bfs():
    jugs = [122, 121, 124, 28, 89, 73]
    goal = [270, 311, 372, 389]
    start = [0, 0, 0, 0]
    queue = deque([start])
    actions = {tuple(start): []}

    while queue:
        state = queue.popleft()
        if state == goal:
            return actions[tuple(state)]
        for i in range(4):
            for j in range(5):
                if state[i] + jugs[j] <= goal[i] and (i == 0 or state[i] + jugs[j] >= state[i-1]):
                    new_state = list(state)
                    new_state[i] += jugs[j]
                    if tuple(new_state) not in actions:
                        queue.append(new_state)
                        actions[tuple(new_state)] = actions[tuple(state)] + [('+', j+1, i+1)]
            if state[i] > 0:
                new_state = list(state)
                new_state[i] = 0
                if tuple(new_state) not in actions:
                    queue.append(new_state)
                    actions[tuple(new_state)] = actions[tuple(state)] + [('-', i+1, i+1)]
    return None

print(bfs())
