
from collections import deque

def bfs(jug_capacities, bucket_capacities):
    initial_state = (0, 0, 0, 0) + tuple(jug_capacities)
    queue = deque([initial_state])
    parents = {initial_state: None}

    while queue:
        state = queue.popleft()
        if state[4:] == bucket_capacities:
            return state

        for i in range(4):
            for j in range(4, 7):
                if state[i] + state[j] <= bucket_capacities[i]:
                    new_state = list(state)
                    new_state[i] += state[j]
                    new_state[j] = 0
                    new_tuple = tuple(new_state)
                    if new_tuple not in parents:
                        queue.append(new_tuple)
                        parents[new_tuple] = state

    return None

def actions(jug_capacities, bucket_capacities):
    state = bfs(jug_capacities, bucket_capacities)
    actions = []
    while state is not None:
        parent = parents[state]
        for i in range(4):
            if state[i] > parent[i]:
                actions.append(('+', state[i] - parent[i], i + 1))
            elif state[i] < parent[i]:
                actions.append(('-', parent[i] - state[i], i + 1))
        state = parent
    return actions[::-1]

jug_capacities = [98, 121, 131, 126, 141, 125, 20]
bucket_capacities = [309, 395, 407, 429]

print(actions(jug_capacities, bucket_capacities))
