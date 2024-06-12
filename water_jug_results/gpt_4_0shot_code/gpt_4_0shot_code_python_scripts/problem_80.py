
from collections import deque

jugs = [110, 146, 117, 118, 148, 104, 79, 103]
buckets = [278, 378, 457, 462]
actions = [('+', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))] + [('-', i+1, j+1) for i in range(len(jugs)) for j in range(len(buckets))]

def is_valid(state):
    return all(state[i] <= state[i+1] for i in range(len(state)-1))

def bfs():
    visited = set()
    queue = deque([([0]*len(buckets), [])])
    while queue:
        state, action_list = queue.popleft()
        if state == buckets:
            return action_list
        for action in actions:
            new_state = state[:]
            if action[0] == '+':
                new_state[action[2]-1] += jugs[action[1]-1]
            else:
                new_state[action[2]-1] -= jugs[action[1]-1]
            new_state[action[2]-1] = max(0, min(new_state[action[2]-1], buckets[action[2]-1]))
            if is_valid(new_state) and tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append((new_state, action_list + [action]))
    return None

print(bfs())
