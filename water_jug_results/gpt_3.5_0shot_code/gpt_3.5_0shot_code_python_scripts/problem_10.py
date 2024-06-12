
from queue import Queue

def pour_water(jugs, target):
    visited = set()
    q = Queue()
    q.put((0, 0, 0, []))  # (bucket1, bucket2, bucket3, actions)

    while not q.empty():
        bucket1, bucket2, bucket3, actions = q.get()

        if bucket1 == target[0] and bucket2 == target[1] and bucket3 == target[2]:
            return actions

        for jug in jugs:
            if jug not in actions:
                if bucket1 + jug <= target[0] and (bucket1 + jug, bucket2, bucket3) not in visited:
                    q.put((bucket1 + jug, bucket2, bucket3, actions + [(f'+', jug, 1)]))
                    visited.add((bucket1 + jug, bucket2, bucket3))
                if bucket2 + jug <= target[1] and bucket2 + jug <= bucket1 and (bucket1, bucket2 + jug, bucket3) not in visited:
                    q.put((bucket1, bucket2 + jug, bucket3, actions + [(f'+', jug, 2)]))
                    visited.add((bucket1, bucket2 + jug, bucket3))
                if bucket3 + jug <= target[2] and bucket3 + jug <= bucket2 and (bucket1, bucket2, bucket3 + jug) not in visited:
                    q.put((bucket1, bucket2, bucket3 + jug, actions + [(f'+', jug, 3)]))
                    visited.add((bucket1, bucket2, bucket3 + jug))

    return None

jugs = [14, 119, 62, 18, 133, 13]
target = [218, 272, 314]

actions = pour_water(jugs, target)
print(actions)
