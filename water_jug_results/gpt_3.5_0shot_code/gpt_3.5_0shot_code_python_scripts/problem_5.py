
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, 0, 0, [])])  # (bucket1, bucket2, bucket3, actions)

    while queue:
        b1, b2, b3, actions = queue.popleft()

        if (b1, b2, b3) == target:
            return actions

        if (b1, b2, b3) in visited:
            continue
        visited.add((b1, b2, b3))

        for jug in jugs:
            if b1 + jug <= target[0]:
                queue.append((b1 + jug, b2, b3, actions + [('+', jug, 1)]))
            if b2 + jug <= target[1] and b2 + jug <= b1:
                queue.append((b1, b2 + jug, b3, actions + [('+', jug, 2)]))
            if b3 + jug <= target[2] and b3 + jug <= b2:
                queue.append((b1, b2, b3 + jug, actions + [('+', jug, 3)]))
            if b1 - jug >= 0:
                queue.append((b1 - jug, b2, b3, actions + [('-', jug, 1)]))
            if b2 - jug >= 0 and b2 - jug >= b1:
                queue.append((b1, b2 - jug, b3, actions + [('-', jug, 2)]))
            if b3 - jug >= 0 and b3 - jug >= b2:
                queue.append((b1, b2, b3 - jug, actions + [('-', jug, 3)]))

    return None

jugs = [145, 101, 17, 75, 102, 129]
target = (260, 287, 413)

actions = pour_water(jugs, target)
print(actions)
