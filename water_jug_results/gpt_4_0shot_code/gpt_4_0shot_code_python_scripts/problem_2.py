
from collections import deque

def bfs(start, end, capacities):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state == end:
            return path
        for i in range(3):
            for j in range(5):
                if state[i] + capacities[j] <= end[i] and all(state[i] + capacities[j] <= state[k] for k in range(i+1, 3)):
                    new_state = list(state)
                    new_state[i] += capacities[j]
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [('+', capacities[j], i+1)]))
                if state[i] - capacities[j] >= 0 and all(state[k] <= state[i] - capacities[j] for k in range(i)):
                    new_state = list(state)
                    new_state[i] -= capacities[j]
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [('-', capacities[j], i+1)]))
    return []

capacities = [31, 102, 53, 33, 32, 24]
start = (0, 0, 0)
end = (188, 198, 289)
print(bfs(start, end, capacities))
