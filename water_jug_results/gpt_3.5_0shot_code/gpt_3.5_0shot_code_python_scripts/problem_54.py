
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        for i in range(3):
            bucket = buckets[i]
            jug = perm[i]
            if bucket + jug <= buckets[i+1]:
                actions.append(('+', jug, i+1))
                bucket += jug
            else:
                actions.append(('+', buckets[i+1] - bucket, i+1))
                actions.append(('-', buckets[i+1] - bucket, i))
                bucket = buckets[i+1]
            buckets[i] = bucket
    return actions

jugs = [45, 67, 134, 133, 86, 66, 107, 94, 124, 122]
buckets = [0, 0, 0, 229, 303, 307]

actions = pour_water(jugs, buckets)

print(actions)
