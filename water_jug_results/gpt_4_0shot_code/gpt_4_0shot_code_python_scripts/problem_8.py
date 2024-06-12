
from collections import deque

jugs = [59, 68, 104, 106, 69, 42]
buckets = [196, 210, 238]
actions = [('+', x, y) for x in jugs for y in range(3)] + [('-', x, y) for x in jugs for y in range(3)]

def bfs():
    queue = deque([([0, 0, 0], [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            new_state = state.copy()
            if action[0] == '+':
                new_state[action[2]] += action[1]
            else:
                new_state[action[2]] -= action[1]
            if new_state[action[2]] < 0 or new_state[action[2]] > buckets[action[2]]:
                continue
            if action[2] > 0 and new_state[action[2]] < new_state[action[2]-1]:
                continue
            if action[2] < 2 and new_state[action[2]] > new_state[action[2]+1]:
                continue
            if tuple(new_state) in visited:
                continue
            queue.append((new_state, path + [action]))
            visited.add(tuple(new_state))

print(bfs())
