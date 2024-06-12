
from itertools import permutations

def pour_water(jugs, buckets):
    def pour(jug, bucket, actions):
        if jug[1] >= buckets[bucket]:
            jug[1] -= buckets[bucket]
            actions.append(('-', jug[0], bucket))
            buckets[bucket] = 0
        else:
            buckets[bucket] -= jug[1]
            actions.append(('-', jug[0], bucket))
            jug[1] = 0

    def fill(jug, bucket, actions):
        if jug[1] >= buckets[bucket]:
            jug[1] -= buckets[bucket]
            actions.append(('+', jug[0], bucket))
            buckets[bucket] = jug[1]
        else:
            buckets[bucket] -= jug[1]
            actions.append(('+', jug[0], bucket))
            buckets[bucket] = jug[1]

    actions = []
    for perm in permutations(jugs):
        buckets_copy = buckets.copy()
        for jug in perm:
            for bucket in range(len(buckets)):
                if buckets[bucket] > 0:
                    pour(jug, bucket, actions)
                if buckets[bucket] == 0:
                    fill(jug, bucket, actions)
                if buckets == [0, 0, 0]:
                    return actions

jugs = [(1, 111), (2, 84), (3, 17), (4, 22), (5, 63), (6, 75), (7, 148), (8, 64)]
buckets = [253, 280, 448]

actions = pour_water(jugs, buckets)
print(actions)
