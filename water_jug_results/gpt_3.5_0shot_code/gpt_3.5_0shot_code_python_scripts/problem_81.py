
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

jugs = {127: 0, 96: 1, 108: 2, 126: 3, 132: 4, 139: 5, 146: 6, 14: 7}
buckets = [273, 349, 435, 503]

result = pour_water(jugs, buckets)
print(result)
