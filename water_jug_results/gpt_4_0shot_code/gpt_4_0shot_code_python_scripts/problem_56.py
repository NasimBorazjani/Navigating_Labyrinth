
from collections import deque

jugs = [12, 88, 148, 87, 143, 131]
buckets = [260, 295, 331, 394]

def valid(state):
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            return False
    return True

def bfs():
    start = [0, 0, 0, 0]
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state == buckets:
            return actions
        for i in range(4):
            for j in range(5):
                if state[i] + jugs[j] <= buckets[i]:
                    new_state = state.copy()
                    new_state[i] += jugs[j]
                    if valid(new_state) and tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('+', jugs[j], i+1)]))
                if state[i] - jugs[j] >= 0:
                    new_state = state.copy()
                    new_state[i] -= jugs[j]
                    if valid(new_state) and tuple(new_state) not in visited:
                        queue.append((new_state, actions + [('-', jugs[j], i+1)]))
        visited.add(tuple(state))
    return None

print(bfs())
