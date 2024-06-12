
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(3):
                if temp_buckets[i] + jug <= buckets[i]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
                    if temp_buckets == buckets:
                        return temp_actions
    return None

jugs = [120, 95, 49, 150, 83, 97, 44, 43]
buckets = [225, 334, 381]

result = pour_water(jugs, buckets)
print(result)
