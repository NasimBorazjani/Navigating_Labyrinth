
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

jugs = {67: 0, 98: 1, 66: 2, 59: 3, 37: 4, 61: 5, 128: 6, 92: 7}
buckets = [308, 309, 387, 433]

result = pour_water(jugs, buckets)
print(result)
