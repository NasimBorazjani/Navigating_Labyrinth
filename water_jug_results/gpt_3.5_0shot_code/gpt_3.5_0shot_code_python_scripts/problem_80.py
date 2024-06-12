
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

jugs = {110: 0, 146: 0, 117: 0, 118: 0, 148: 0, 104: 0, 79: 0, 103: 0}
buckets = [278, 378, 457, 462]

actions = pour_water(jugs, buckets)
print(actions)
