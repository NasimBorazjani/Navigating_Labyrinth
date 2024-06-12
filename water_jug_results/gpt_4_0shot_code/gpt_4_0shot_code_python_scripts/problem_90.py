
from collections import deque

jugs = [88, 125, 100, 62, 134, 89, 33, 133]
buckets = [306, 407, 457, 518]
actions = []

def bfs():
    queue = deque([([0]*4, [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        if state == buckets:
            return action

        for i in range(len(jugs)):
            for j in range(len(state)):
                if state[j] + jugs[i] <= buckets[j] and (j == 0 or state[j] + jugs[i] <= state[j-1]):
                    new_state = state.copy()
                    new_state[j] += jugs[i]
                    new_action = action + [('+', jugs[i], j+1)]
                    queue.append((new_state, new_action))

                if state[j] - jugs[i] >= 0:
                    new_state = state.copy()
                    new_state[j] -= jugs[i]
                    new_action = action + [('-', jugs[i], j+1)]
                    queue.append((new_state, new_action))

    return None

actions = bfs()
print(actions)
