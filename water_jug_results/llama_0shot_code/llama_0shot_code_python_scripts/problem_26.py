
from collections import deque

def bfs(capacities, targets):
    initial_state = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    queue = deque([initial_state])
    parents = {initial_state: None}
    while queue:
        state = queue.popleft()
        if state[3:] == targets:
            break
        for i in range(len(capacities)):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        new_state = list(state)
                        new_state[7 + j] += capacities[i]
                        new_state[7 + k] -= capacities[i]
                        if new_state[7 + j] >= 0 and new_state[7 + k] >= 0:
                            new_state = tuple(new_state)
                            if new_state not in parents:
                                queue.append(new_state)
                                parents[new_state] = state
    if state[3:] != targets:
        return None
    actions = []
    while state is not None:
        parent = parents[state]
        for i in range(len(capacities)):
            if state[i] > parent[i]:
                actions.append(('+', capacities[i], i + 1))
                break
            elif state[i] < parent[i]:
                actions.append(('-', capacities[i], i + 1))
                break
        state = parent
    return actions[::-1]

capacities = [24, 132, 149, 62, 120, 61, 42]
targets = [298, 430, 468]
print(bfs(capacities, targets))
