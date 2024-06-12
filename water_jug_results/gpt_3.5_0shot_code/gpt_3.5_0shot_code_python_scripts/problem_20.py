
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
    
    min_actions = min(actions, key=len)
    return min_actions

jugs = {76, 48, 35, 94, 93, 115, 16, 53}
buckets = [247, 261, 273]

result = pour_water(jugs, buckets)
print(result)