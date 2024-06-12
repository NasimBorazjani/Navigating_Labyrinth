
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
        actions.append(temp_actions)
    
    return min(actions, key=len)

jugs = {15, 20, 141, 104, 67, 14}
buckets = [230, 267, 278, 318]

result = pour_water(jugs, buckets)
print(result)
