
from collections import deque

def bfs(start, target, capacities):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for i in range(len(state)):
            for j in range(len(capacities)):
                if state[i] + capacities[j] <= target[i] and all(state[i] + capacities[j] <= state[k] for k in range(i+1, len(state))):
                    new_state = list(state)
                    new_state[i] += capacities[j]
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        queue.append((new_state, path + [('+', capacities[j], i+1)]))
                        visited.add(new_state)
                if state[i] - capacities[j] >= 0 and all(state[i] - capacities[j] >= state[k] for k in range(0, i)):
                    new_state = list(state)
                    new_state[i] -= capacities[j]
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        queue.append((new_state, path + [('-', capacities[j], i+1)]))
                        visited.add(new_state)
    return None

start = (0, 0, 0)
target = (168, 239, 307)
capacities = [33, 56, 108, 53, 65, 54, 52, 59]
print(bfs(start, target, capacities))
