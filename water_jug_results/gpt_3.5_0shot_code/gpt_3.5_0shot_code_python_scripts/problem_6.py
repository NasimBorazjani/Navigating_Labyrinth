
from collections import deque

def pour_water(jugs, target):
    visited = set()
    q = deque([(0, 0, 0, [])])

    while q:
        a, b, c, actions = q.popleft()

        if (a, b, c) == target:
            return actions

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        for jug in jugs:
            if a < jug:
                q.append((jug, b, c, actions + [('+', jug, 1)]))
            if b < jug:
                q.append((a, jug, c, actions + [('+', jug, 2)]))
            if c < jug:
                q.append((a, b, jug, actions + [('+', jug, 3)]))

            if a > 0:
                q.append((0, b, c, actions + [('-', a, 1)]))
            if b > 0:
                q.append((a, 0, c, actions + [('-', b, 2)]))
            if c > 0:
                q.append((a, b, 0, actions + [('-', c, 3)]))

    return None

jugs = [76, 135, 134, 19, 10, 30]
target = (390, 420, 439)

actions = pour_water(jugs, target)
print(actions)
