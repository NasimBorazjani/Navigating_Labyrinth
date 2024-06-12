
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

jugs = {22, 48, 29, 111, 92, 28}
buckets = [164, 233, 289]

result = pour_water(jugs, buckets)
print(result)
