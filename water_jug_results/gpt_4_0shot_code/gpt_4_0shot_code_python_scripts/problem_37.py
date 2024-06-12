
from collections import deque

jugs = [19, 122, 104, 145, 38, 141, 126, 82, 37, 33]
buckets = [256, 399, 410]
actions = [(i, j) for i in range(len(jugs)) for j in range(len(buckets))]

def bfs():
    start = (0, 0, 0)
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == buckets:
            return path
        for action in actions:
            i, j = action
            next_state = list(state)
            if next_state[j] + jugs[i] <= buckets[j] and (j == 0 or next_state[j] + jugs[i] <= next_state[j - 1]):
                next_state[j] += jugs[i]
                next_path = path + [('+', i + 1, j + 1)]
                if tuple(next_state) not in visited:
                    queue.append((tuple(next_state), next_path))
                    visited.add(tuple(next_state))
            if next_state[j] - jugs[i] >= 0 and (j == len(buckets) - 1 or next_state[j] - jugs[i] >= next_state[j + 1]):
                next_state[j] -= jugs[i]
                next_path = path + [('-', i + 1, j + 1)]
                if tuple(next_state) not in visited:
                    queue.append((tuple(next_state), next_path))
                    visited.add(tuple(next_state))
    return None

print(bfs())
