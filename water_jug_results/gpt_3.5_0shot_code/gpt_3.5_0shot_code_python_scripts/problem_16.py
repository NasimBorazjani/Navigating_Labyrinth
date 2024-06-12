
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        for i in range(3):
            if perm[i] >= buckets[i]:
                actions.append(('+', perm[i], i+1))
                perm = list(perm)
                perm[i] -= buckets[i]
                break
        if perm[0] == buckets[0] and perm[1] == buckets[1] and perm[2] == buckets[2]:
            return actions
    return None

jugs = [102, 130, 82, 131, 133, 116]
buckets = [265, 368, 378]

result = pour_water(jugs, buckets)
print(result)
