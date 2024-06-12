
from collections import deque

jugs = [121, 87, 150, 52, 43, 139, 90, 44, 59, 146]
buckets = [249, 446, 530]
actions = [(f'{sign}', i+1, j+1) for sign in '+-' for i in range(len(jugs)) for j in range(len(buckets))]

def is_valid(state):
    return all(x <= y for x, y in zip(state, state[1:]))

def perform_action(state, action):
    sign, i, j = action
    i -= 1
    j -= 1
    if sign == '+':
        if state[j] + jugs[i] <= buckets[j]:
            state = state[:]
            state[j] += jugs[i]
    else:
        if state[j] >= jugs[i]:
            state = state[:]
            state[j] -= jugs[i]
    return state if is_valid(state) else None

def solve():
    start = [0, 0, 0]
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            next_state = perform_action(state, action)
            if next_state is not None and tuple(next_state) not in visited:
                queue.append((next_state, path + [action]))
                visited.add(tuple(next_state))
    return None

print(solve())
