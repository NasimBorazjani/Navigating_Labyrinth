
from collections import deque

def bfs(jug_capacities, bucket_capacities):
    initial_state = (0, 0, 0, 0, 0) + tuple(bucket_capacities)
    final_state = (0, 0, 0, 0, 0) + (0, 0, 0, 0)

    queue = deque([((), initial_state)])

    while queue:
        actions, state = queue.popleft()

        if state == final_state:
            return actions

        for i in range(len(jug_capacities)):
            for j in range(len(bucket_capacities)):
                for action in ['+', '-']:
                    if action == '+':
                        new_state = list(state)
                        new_state[i] += min(jug_capacities[i] - new_state[i], bucket_capacities[j] - state[j + 5])
                        new_state[j + 5] += min(jug_capacities[i] - new_state[i], bucket_capacities[j] - state[j + 5])
                        new_state = tuple(new_state)
                    else:
                        new_state = list(state)
                        new_state[j + 5] -= min(new_state[j + 5], jug_capacities[i] - new_state[i])
                        new_state[i] -= min(new_state[j + 5], jug_capacities[i] - new_state[i])
                        new_state = tuple(new_state)

                    if new_state not in queue:
                        queue.append((actions + ((action, i, j + 5),), new_state))

    return None

jug_capacities = [14, 42, 113, 131, 41, 147]
bucket_capacities = [240, 257, 350, 369]

actions = bfs(jug_capacities, bucket_capacities)
print(actions)
