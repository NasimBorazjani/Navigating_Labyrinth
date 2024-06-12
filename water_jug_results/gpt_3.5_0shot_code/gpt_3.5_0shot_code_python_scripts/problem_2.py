
from collections import deque

def pour_water(jugs, target):
    visited = set()
    queue = deque([(0, 0, 0, [])])  # (bucket1, bucket2, bucket3, actions)

    while queue:
        bucket1, bucket2, bucket3, actions = queue.popleft()

        if (bucket1, bucket2, bucket3) == target:
            return actions

        for jug in jugs:
            new_actions = actions.copy()

            # Fill bucket
            if jug == bucket1:
                if bucket2 <= bucket1 + jug:
                    new_bucket2 = bucket2 + bucket1
                    new_bucket1 = 0
                else:
                    new_bucket2 = jug
                    new_bucket1 = bucket1 - (jug - bucket2)
                if (new_bucket1, new_bucket2, bucket3) not in visited:
                    queue.append((new_bucket1, new_bucket2, bucket3, new_actions + [('+', jug, 1)]))

            # Pour water from bucket2 to bucket1
            if jug == bucket2:
                if bucket1 <= bucket2 + jug:
                    new_bucket1 = bucket1 + bucket2
                    new_bucket2 = 0
                else:
                    new_bucket1 = jug
                    new_bucket2 = bucket2 - (jug - bucket1)
                if (new_bucket1, new_bucket2, bucket3) not in visited:
                    queue.append((new_bucket1, new_bucket2, bucket3, new_actions + [('+', jug, 2)]))

            # Pour water from bucket2 to bucket3
            if jug == bucket2:
                if bucket3 <= bucket2 + jug:
                    new_bucket3 = bucket3 + bucket2
                    new_bucket2 = 0
                else:
                    new_bucket3 = jug
                    new_bucket2 = bucket2 - (jug - bucket3)
                if (bucket1, new_bucket2, new_bucket3) not in visited:
                    queue.append((bucket1, new_bucket2, new_bucket3, new_actions + [('+', jug, 3)]))

            visited.add((bucket1, bucket2, bucket3))

    return None

jugs = [31, 102, 53, 33, 32, 24]
target = (188, 198, 289)

actions = pour_water(jugs, target)
print(actions)
