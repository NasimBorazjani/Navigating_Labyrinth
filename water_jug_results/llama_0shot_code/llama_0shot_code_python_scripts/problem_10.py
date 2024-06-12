
from collections import deque

def bfs():
    # Initial state: all buckets are empty
    initial_state = ([0, 0, 0], [14, 119, 62, 18, 133, 13])
    # Final states: the amounts of water in the buckets
    final_states = [[218, 272, 314], [314, 272, 218]]
    # Queue of states to be explored
    queue = deque([(initial_state, [])])
    # Set of visited states to avoid visiting the same state multiple times
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        buckets, jugs = state
        if buckets in final_states:
            return actions
        for i in range(len(jugs)):
            for j in range(len(buckets)):
                # Try adding water from jug i to bucket j
                new_buckets = list(buckets)
                new_buckets[j] += min(jugs[i], max(0, 314 - sum(buckets) + buckets[j]))
                new_jugs = list(jugs)
                new_jugs[i] -= min(jugs[i], max(0, 314 - sum(buckets) + buckets[j]))
                new_state = (tuple(new_buckets), tuple(new_jugs))
                queue.append((new_state, actions + [('+', jugs[i], j+1)]))
                # Try removing water from bucket j to jug i
                new_buckets = list(buckets)
                new_buckets[j] -= min(buckets[j], jugs[i])
                new_jugs = list(jugs)
                new_jugs[i] += min(buckets[j], jugs[i])
                new_state = (tuple(new_buckets), tuple(new_jugs))
                queue.append((new_state, actions + [('-', jugs[i], j+1)]))

print(bfs())
