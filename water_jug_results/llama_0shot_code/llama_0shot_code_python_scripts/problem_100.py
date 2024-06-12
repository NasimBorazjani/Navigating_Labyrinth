
from collections import deque

def bfs(capacities, targets):
    initial_state = [0] * len(targets)
    goal_state = targets
    queue = deque([(initial_state, [])])
    shortest_path = {tuple(initial_state): []}
    
    while queue:
        state, actions = queue.popleft()
        if state == goal_state:
            return actions
        for i, (capacity, target) in enumerate(zip(capacities, targets)):
            for j, (next_capacity, next_target) in enumerate(zip(capacities, targets)):
                if next_capacity >= target - state[i] and state[i] <= state[j]:
                    next_state = list(state)
                    next_state[i] += min(target - state[i], next_capacity)
                    next_state[j] -= min(target - state[i], next_capacity)
                    next_state = tuple(next_state)
                    if next_state not in shortest_path:
                        queue.append((next_state, actions + [('+', capacity, i+1)]))
                        shortest_path[next_state] = actions + [('+', capacity, i+1)]
                    if next_state[i] > target:
                        next_state[i] -= min(next_state[i] - target, next_state[j])
                        next_state[j] += min(next_state[i] - target, next_state[j])
                        next_state = tuple(next_state)
                        if next_state not in shortest_path:
                            queue.append((next_state, actions + [('-', capacity, i+1)]))
                            shortest_path[next_state] = actions + [('-', capacity, i+1)]
    return []

capacities = [126, 120, 127, 110, 54, 39, 38, 47, 139, 99]
targets = [219, 240, 312, 411]

actions = bfs(capacities, targets)
print(actions)
