
from collections import deque

def bfs(start, target, jugs):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (buckets, actions) = queue.popleft()
        if buckets == target:
            return actions
        for i, jug in enumerate(jugs):
            for j, bucket in enumerate(buckets):
                if bucket + jug <= target[j]:
                    new_buckets = list(buckets)
                    new_buckets[j] += jug
                    new_buckets = tuple(new_buckets)
                    if new_buckets not in visited:
                        visited.add(new_buckets)
                        queue.append((new_buckets, actions + [('+', jug, j+1)]))
                if bucket - jug >= 0:
                    new_buckets = list(buckets)
                    new_buckets[j] -= jug
                    new_buckets = tuple(new_buckets)
                    if new_buckets not in visited:
                        visited.add(new_buckets)
                        queue.append((new_buckets, actions + [('-', jug, j+1)]))
    return None

jugs = [126, 120, 127, 110, 54, 39, 38, 47, 139, 99]
buckets = [0, 0, 0, 0]
target = [219, 240, 312, 411]

print(bfs(buckets, target, jugs))
