
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

jugs = {36: 0, 88: 0, 132: 0, 70: 0, 87: 0, 111: 0}
buckets = [225, 237, 243]

result = pour_water(jugs, buckets)
print(result)
