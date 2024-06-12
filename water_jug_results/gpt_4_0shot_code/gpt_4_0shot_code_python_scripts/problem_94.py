
from collections import deque

def solve():
    jugs = [81, 56, 41, 88, 137, 14, 149, 120, 87, 104]
    goal = [377, 456, 512, 541]
    start = [0, 0, 0, 0]
    queue = deque([start])
    actions = {tuple(start): []}

    while queue:
        state = queue.popleft()
        if state == goal:
            return actions[tuple(state)]
        for i in range(4):
            for j in range(9):
                if state[i] + jugs[j] <= goal[i] and (i == 3 or state[i] + jugs[j] <= state[i+1]):
                    new_state = list(state)
                    new_state[i] += jugs[j]
                    action = ('+', j+1, i+1)
                    if tuple(new_state) not in actions:
                        actions[tuple(new_state)] = actions[tuple(state)] + [action]
                        queue.append(new_state)
                if state[i] > 0:
                    new_state = list(state)
                    new_state[i] = 0
                    action = ('-', j+1, i+1)
                    if tuple(new_state) not in actions:
                        actions[tuple(new_state)] = actions[tuple(state)] + [action]
                        queue.append(new_state)
    return None

print(solve())
