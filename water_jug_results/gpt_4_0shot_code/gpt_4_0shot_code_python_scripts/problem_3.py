
from collections import deque

def bfs():
    jugs = [43, 149, 131, 132, 70, 104]
    goal = [284, 297, 436]
    visited = set()
    queue = deque([([], [0, 0, 0])])

    while queue:
        actions, buckets = queue.popleft()
        if buckets == goal:
            return actions
        for i, jug in enumerate(jugs):
            for j in range(3):
                if buckets[j] + jug <= goal[j] and all(buckets[k] <= buckets[j] + jug for k in range(j+1, 3)):
                    new_buckets = buckets[:]
                    new_buckets[j] += jug
                    new_state = (tuple(new_buckets), ('+', i+1, j+1))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((actions + [new_state[1]], new_buckets))
                if buckets[j] > 0:
                    new_buckets = buckets[:]
                    new_buckets[j] = 0
                    new_state = (tuple(new_buckets), ('-', i+1, j+1))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((actions + [new_state[1]], new_buckets))

print(bfs())
