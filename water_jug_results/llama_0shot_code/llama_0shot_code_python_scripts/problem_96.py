
from collections import deque

def bfs(capacities, targets):
    initial_state = (0,) * len(targets)
    queue = deque([(initial_state, None)])
    parents = {initial_state: None}
    while queue:
        current_state, actions = queue.popleft()
        if current_state == tuple(targets):
            return actions
        for i, (capacity, target) in enumerate(zip(capacities, targets)):
            for action in [('+', capacity, i), ('-', capacity, i)]:
                if action[0] == '+' and current_state[i] + capacity <= target:
                    next_state = list(current_state)
                    next_state[i] += capacity
                    next_state = tuple(next_state)
                    if next_state not in parents:
                        queue.append((next_state, actions + [action]))
                        parents[next_state] = actions
                elif action[0] == '-' and current_state[i] - capacity >= 0:
                    next_state = list(current_state)
                    next_state[i] -= capacity
                    next_state = tuple(next_state)
                    if next_state not in parents:
                        queue.append((next_state, actions + [action]))
                        parents[next_state] = actions
    return None

capacities = [90, 21, 104, 111, 97, 22, 34, 15, 62, 52]
targets = [177, 263, 294, 462]
actions = bfs(capacities, targets)
print(actions)
