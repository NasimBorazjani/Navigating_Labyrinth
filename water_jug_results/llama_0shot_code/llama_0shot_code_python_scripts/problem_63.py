
from collections import deque

def bfs(jugs, buckets, capacity):
    # Initial state
    start = ([0]*len(buckets), jugs)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (state, actions) = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state[0] == buckets:
                return actions
            for i, (jug, amount) in enumerate(zip(jugs, state[0])):
                if amount < buckets[i]:
                    # Fill the bucket
                    new_state = (list(state[0]), list(state[1]))
                    new_state[0][i] += min(capacity[i] - amount, buckets[i] - amount)
                    new_state[1][i] -= min(capacity[i] - amount, buckets[i] - amount)
                    queue.append((new_state, actions + [('+', capacity[i], i+1)]))
                if amount > 0:
                    # Empty the bucket
                    new_state = (list(state[0]), list(state[1]))
                    new_state[0][i] -= min(amount, state[1][i])
                    new_state[1][i] += min(amount, state[1][i])
                    queue.append((new_state, actions + [('-', capacity[i], i+1)]))

    return None

# Problem parameters
jugs = [123, 124, 133, 85, 74]
buckets = [276, 277, 355, 425]
capacity = [123, 124, 133, 85, 74]

# Solve the problem
solution = bfs(jugs, buckets, capacity)
print(solution)
