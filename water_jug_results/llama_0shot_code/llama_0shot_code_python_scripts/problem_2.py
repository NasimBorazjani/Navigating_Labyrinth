
from collections import deque

def bfs():
    initial_state = [0, 0, 0]
    goal_state = [188, 198, 289]
    capacities = [31, 102, 53, 33, 32, 24]
    actions = [('+', c, i+1) for i, c in enumerate(capacities)] + [('-', c, i+1) for i, c in enumerate(capacities)] + [(str(min(capacities[i], goal_state[j-1]-initial_state[j-1])), capacities[i], j) for i, c in enumerate(capacities) for j in range(1, 4)]
    queue = deque([([0, 0, 0], [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for action in actions:
            if action[1] in capacities:
                new_state = list(state)
                if action[0] == '+':
                    new_state[action[2]-1] += action[1]
                elif action[0] == '-':
                    new_state[action[2]-1] -= action[1]
                else:
                    new_state[int(action[2])-1] += int(action[0])
                    new_state[action[2]-1] -= int(action[0])
                if new_state not in visited and all(0 <= new_state[i] <= goal_state[i] for i in range(3)):
                    visited.add(tuple(new_state))
                    queue.append((new_state, path + [action]))
    return None

print(bfs())
