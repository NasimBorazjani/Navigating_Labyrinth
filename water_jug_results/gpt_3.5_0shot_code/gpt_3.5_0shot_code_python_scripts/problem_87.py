
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(len(temp_buckets)):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_actions.append(('+', jug, i+1))
                    temp_buckets[i] += jug
                    if temp_buckets == buckets:
                        return temp_actions
    return None

jugs = [36, 95, 47, 149, 58, 96, 81, 148]
buckets = [252, 307, 412, 431]

result = pour_water(jugs, buckets)
print(result)
