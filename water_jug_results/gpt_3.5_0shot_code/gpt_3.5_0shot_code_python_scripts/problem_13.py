
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, 0, 0, [])])  # (bucket1, bucket2, bucket3, actions)

    while queue:
        bucket1, bucket2, bucket3, actions = queue.popleft()

        if (bucket1, bucket2, bucket3) == target:
            return actions

        if (bucket1, bucket2, bucket3) in visited:
            continue
        visited.add((bucket1, bucket2, bucket3))

        for jug in jugs:
            if bucket1 + jug <= target[0] and bucket1 + jug >= bucket2:
                queue.append((bucket1 + jug, bucket2, bucket3, actions + [('+', jug, 1)]))
            if bucket2 + jug <= target[1] and bucket2 + jug >= bucket3:
                queue.append((bucket1, bucket2 + jug, bucket3, actions + [('+', jug, 2)]))
            if bucket3 + jug <= target[2]:
                queue.append((bucket1, bucket2, bucket3 + jug, actions + [('+', jug, 3)]))
            if bucket1 - jug >= 0 and bucket1 - jug >= bucket2:
                queue.append((bucket1 - jug, bucket2, bucket3, actions + [('-', jug, 1)]))
            if bucket2 - jug >= 0 and bucket2 - jug >= bucket3:
                queue.append((bucket1, bucket2 - jug, bucket3, actions + [('-', jug, 2)]))
            if bucket3 - jug >= 0:
                queue.append((bucket1, bucket2, bucket3 - jug, actions + [('-', jug, 3)]))

    return None

jugs = [57, 84, 47, 76, 85, 69]
target = (203, 217, 334)

actions = pour_water(jugs, target)
print(actions)
