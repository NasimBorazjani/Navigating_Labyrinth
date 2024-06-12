
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, 0, 0, [])])  # (bucket1, bucket2, bucket3, actions)

    while queue:
        bucket1, bucket2, bucket3, actions = queue.popleft()

        if (bucket1, bucket2, bucket3) == target:
            return actions

        for jug in jugs:
            for i in range(3):
                if i == 0:
                    new_bucket1 = jug
                    new_bucket2 = bucket2
                    new_bucket3 = bucket3
                elif i == 1:
                    new_bucket1 = bucket1
                    new_bucket2 = jug
                    new_bucket3 = bucket3
                else:
                    new_bucket1 = bucket1
                    new_bucket2 = bucket2
                    new_bucket3 = jug

                if new_bucket1 <= new_bucket2 <= new_bucket3 and (new_bucket1, new_bucket2, new_bucket3) not in visited:
                    visited.add((new_bucket1, new_bucket2, new_bucket3))
                    queue.append((new_bucket1, new_bucket2, new_bucket3, actions + [('+', jug, i+1)]))

    return None

jugs = [144, 37, 73, 79, 75, 74]
target = (236, 333, 386)

actions = pour_water(jugs, target)
print(actions)
