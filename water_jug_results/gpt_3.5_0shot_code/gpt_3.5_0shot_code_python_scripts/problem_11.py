
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, 0, 0, [])])  # (bucket 1, bucket 2, bucket 3, actions)

    while queue:
        b1, b2, b3, actions = queue.popleft()

        if (b1, b2, b3) == target:
            return actions

        for jug in jugs:
            if b1 + jug <= target[0] and (b1 + jug, b2, b3) not in visited:
                queue.append((b1 + jug, b2, b3, actions + [('+', jug, 1)]))
                visited.add((b1 + jug, b2, b3))

            if b2 + jug <= target[1] and b2 + jug <= b1 and (b1, b2 + jug, b3) not in visited:
                queue.append((b1, b2 + jug, b3, actions + [('+', jug, 2)]))
                visited.add((b1, b2 + jug, b3))

            if b3 + jug <= target[2] and b3 + jug <= b2 and (b1, b2, b3 + jug) not in visited:
                queue.append((b1, b2, b3 + jug, actions + [('+', jug, 3)]))
                visited.add((b1, b2, b3 + jug))

    return None

jugs = [140, 58, 129, 130, 125]
target = (391, 401, 431)

actions = pour_water(jugs, target)
print(actions)
