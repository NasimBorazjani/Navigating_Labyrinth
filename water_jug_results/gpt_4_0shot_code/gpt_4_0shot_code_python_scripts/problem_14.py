
from collections import deque

jugs = [144, 37, 73, 79, 75, 74]
buckets = [236, 333, 386]
actions = [('+', x, y) for x in jugs for y in range(3)] + [('-', x, y) for x in jugs for y in range(3)]

def is_valid(state):
    return all(state[i] <= state[i+1] for i in range(2))

def bfs():
    queue = deque([([0, 0, 0], [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            new_state = state[:]
            if action[0] == '+':
                new_state[action[2]] += action[1]
            else:
                new_state[action[2]] -= action[1]
            new_state[action[2]] = max(0, min(new_state[action[2]], buckets[action[2]]))
            if is_valid(new_state) and tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))
                visited.add(tuple(new_state))
    return None

print(bfs())
