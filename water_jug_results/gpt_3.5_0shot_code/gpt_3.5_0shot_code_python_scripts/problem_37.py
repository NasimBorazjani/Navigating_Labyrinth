
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(3):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_buckets_new = temp_buckets.copy()
                    temp_buckets_new[i] += jug
                    temp_actions.append(('+', jug, i+1))
                    if temp_buckets_new[i] == buckets[i]:
                        return temp_actions
                    temp_buckets = temp_buckets_new
    return None

jugs = {19, 122, 104, 145, 38, 141, 126, 82, 37, 33}
buckets = [256, 399, 410]

result = pour_water(jugs, buckets)
print(result)
