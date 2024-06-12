
from collections import deque

def bfs(start, target, capacities):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for i, x in enumerate(capacities):
            for j in range(3):
                if state[j] + x <= target[j] and state[j] + x <= (state[j+1] if j < 2 else float('inf')):
                    new_state = list(state)
                    new_state[j] += x
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, path + [('+', x, j+1)]))
                if state[j] - x >= 0 and state[j] - x >= (state[j-1] if j > 0 else 0):
                    new_state = list(state)
                    new_state[j] -= x
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        queue.append((new_state, path + [('-', x, j+1)]))

    return None

capacities = [76, 48, 35, 94, 93, 115, 16, 53]
start = [0, 0, 0]
target = [247, 261, 273]
print(bfs(start, target, capacities))
