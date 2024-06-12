
from collections import deque

def bfs(jug_capacities, target_volumes):
    initial_state = (0, 0, 0), jug_capacities
    final_states = [(target_volumes[0], 0, 0), (target_volumes[1], 0, 0), (target_volumes[2], 0, 0)]
    queue = deque([([], initial_state)])
    visited = set()

    while queue:
        actions, state = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state in final_states:
            return actions
        for i, (b1, b2, b3) in enumerate(state[0]):
            for j, jug in enumerate(state[1]):
                if jug > 0:
                    new_state = list(state[0])
                    new_state[i] = (b1 + min(jug, target_volumes[i] - b1), b2, b3)
                    new_state[1][j] -= min(jug, target_volumes[i] - b1)
                    queue.append((actions + [('+', j, i + 1)], (tuple(new_state), list(state[1]))))
                if b1 > 0:
                    new_state = list(state[0])
                    new_state[i] = (b1 - min(b1, jug), b2, b3)
                    new_state[1][j] += min(b1, jug)
                    queue.append((actions + [('-', j, i + 1)], (tuple(new_state), list(state[1]))))

jug_capacities = [80, 69, 12, 52, 107, 53, 82, 95, 108]
target_volumes = [170, 385, 499]
print(bfs(jug_capacities, target_volumes))
