
from collections import deque

def bfs(jugs, buckets):
    queue = deque([([0]*len(buckets), 0, [])])
    visited = set()
    closest = [float('inf')] * len(buckets)
    steps = [float('inf')] * len(buckets)

    while queue:
        state, step, actions = queue.popleft()
        if state not in visited:
            visited.add(tuple(state))
            total = sum(state)
            if state == buckets:
                return actions
            if total < sum(closest):
                closest[:] = state
                steps[:] = [step] * len(buckets)
            elif total == sum(closest):
                steps[total - sum(buckets) < steps[total - sum(buckets)] - sum(buckets)] = step
            for i, (jug, bucket) in enumerate(zip(jugs, state)):
                if bucket < buckets[i]:
                    queue.append((list(state), step + 1, actions + [('+', jug, i+1)]))
                if state[i] > 0:
                    queue.append((list(state), step + 1, actions + [('-', jug, i+1)]))
    return None

jugs = [116, 16, 79, 75, 30, 87, 28, 96, 15, 134]
buckets = [155, 208, 295]
actions = bfs(jugs, buckets)
print(actions)
