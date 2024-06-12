
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(len(temp_buckets)):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
                    if temp_buckets == buckets:
                        return temp_actions
    return None

jugs = [139, 143, 17, 138, 133, 19, 126, 102, 65]
buckets = [349, 415, 458]

result = pour_water(jugs, buckets)
print(result)
