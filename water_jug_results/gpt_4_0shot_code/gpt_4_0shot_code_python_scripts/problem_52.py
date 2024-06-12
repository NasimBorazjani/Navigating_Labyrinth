
from collections import deque

def bfs(start, target, jugs):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (x, y, z), actions = queue.popleft()
        if (x, y, z) == target:
            return actions
        for i, jug in enumerate(jugs):
            if x + jug <= target[0]:  # fill bucket 1
                state = (x + jug, y, z)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('+', jug, 1)]))
            if y + jug <= target[1] and y + jug >= x:  # fill bucket 2
                state = (x, y + jug, z)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('+', jug, 2)]))
            if z + jug <= target[2] and z + jug >= y:  # fill bucket 3
                state = (x, y, z + jug)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('+', jug, 3)]))
            if x - jug >= 0:  # empty bucket 1
                state = (x - jug, y, z)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('-', jug, 1)]))
            if y - jug >= x:  # empty bucket 2
                state = (x, y - jug, z)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('-', jug, 2)]))
            if z - jug >= y:  # empty bucket 3
                state = (x, y, z - jug)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, actions + [('-', jug, 3)]))

    return None

jugs = [45, 141, 50, 114, 104, 19, 78, 18, 23, 133]
start = (0, 0, 0)
target = (253, 337, 385)
print(bfs(start, target, jugs))
