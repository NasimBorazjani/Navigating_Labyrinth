
from collections import deque

def bfs(jugs, buckets, target):
    queue = deque([([0]*len(buckets), [])])
    visited = set()
    while queue:
        (state, actions) = queue.popleft()
        if state in visited:
            continue
        visited.add(tuple(state))
        if state == target:
            return actions
        for i, (jug, bucket) in enumerate(zip(jugs, state)):
            if bucket < target[i]:
                queue.append((list(state), actions + [('+', jug, i)]))
            if state[i] > 0:
                queue.append(([state[j] - min(state[j], jug) for j in range(len(state))], actions + [('-', jug, i)]))
    return None

jugs = [52, 55, 84, 135, 136, 47, 139, 76]
buckets = [1, 2, 3, 4]
target = [292, 325, 496, 516]

actions = bfs(jugs, buckets, target)
print(actions)
