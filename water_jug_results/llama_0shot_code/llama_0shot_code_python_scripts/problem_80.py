
from collections import deque

def bfs(jug_capacities, bucket_capacities):
    initial_state = ((0, 0, 0, 0), (110, 146, 117, 118, 148, 104, 79, 103))
    queue = deque([initial_state])
    parent = {initial_state: None}

    while queue:
        state = queue.popleft()
        buckets, jugs = state

        if buckets == bucket_capacities:
            actions = []
            while state is not None:
                actions.append(parent[state])
                state = parent[state]
            return actions[::-1]

        for i in range(len(jugs)):
            for j in range(len(buckets)):
                for action in [('+', i, j), ('-', i, j)]:
                    next_buckets, next_jugs = buckets[:], jugs[:]
                    if action[0] == '+':
                        next_buckets[j] += min(jugs[i], bucket_capacities[j] - buckets[j])
                        next_jugs[i] -= min(jugs[i], bucket_capacities[j] - buckets[j])
                    else:
                        next_buckets[j] -= min(buckets[j], jugs[i])
                        next_jugs[i] += min(buckets[j], jugs[i])
                    next_state = (tuple(next_buckets), tuple(next_jugs))
                    if next_state not in parent:
                        queue.append(next_state)
                        parent[next_state] = action
    return None

jug_capacities = [110, 146, 117, 118, 148, 104, 79, 103]
bucket_capacities = [278, 378, 457, 462]

actions = bfs(jug_capacities, bucket_capacities)
print(actions)
