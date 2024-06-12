
from collections import deque

def bfs(initial_state, final_states, actions):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, actions = queue.popleft()
        if state in final_states:
            return actions
        for next_state, action in actions_from_state(state, actions):
            if next_state not in visited:
                queue.append((next_state, actions + [action]))
                visited.add(next_state)

def actions_from_state(state, actions):
    bucket_capacities = [240, 242, 246, 329]
    jug_capacities = [54, 89, 26, 70, 71, 128]
    buckets, jugs = state
    for i, (b, j) in enumerate(zip(bucket_capacities, jug_capacities)):
        if buckets[i] < b and j > 0:
            new_buckets = list(buckets)
            new_buckets[i] += min(j, b - buckets[i])
            new_jugs = list(jugs)
            new_jugs[i] -= min(j, b - buckets[i])
            yield (tuple(new_buckets), tuple(new_jugs)), ('+', j, i)
        if buckets[i] > b and buckets[i] > 0:
            new_buckets = list(buckets)
            new_buckets[i] -= min(buckets[i], buckets[i] - b)
            new_jugs = list(jugs)
            new_jugs[i] += min(buckets[i], buckets[i] - b)
            yield (tuple(new_buckets), tuple(new_jugs)), ('-', j, i)

initial_state = ((0, 0, 0, 0), (54, 89, 26, 70, 71, 128))
final_states = [((240, 242, 246, 329), (54, 89, 26, 70, 71, 128))]

actions = bfs(initial_state, final_states, actions_from_state)
print(actions)
