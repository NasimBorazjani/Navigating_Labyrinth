
from collections import deque

jugs = [146, 45, 136, 13, 148, 17, 42, 137, 141, 31]
buckets = [307, 384, 555, 575]
actions = []

def bfs():
    queue = deque([([0]*4, [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if state == buckets:
            return action
        for i in range(len(jugs)):
            for j in range(len(buckets)):
                if state[j] + jugs[i] <= buckets[j] and all(state[j] + jugs[i] >= state[k] for k in range(j+1, len(buckets))):
                    new_state = state[:]
                    new_state[j] += jugs[i]
                    new_action = action + [('+', jugs[i], j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, new_action))
                        visited.add(tuple(new_state))
                if state[j] - jugs[i] >= 0 and all(state[j] - jugs[i] <= state[k] for k in range(j)):
                    new_state = state[:]
                    new_state[j] -= jugs[i]
                    new_action = action + [('-', jugs[i], j+1)]
                    if tuple(new_state) not in visited:
                        queue.append((new_state, new_action))
                        visited.add(tuple(new_state))
    return []

actions = bfs()
print(actions)
