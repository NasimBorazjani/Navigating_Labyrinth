
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(len(temp_buckets)):
                if temp_buckets[i] + jug <= buckets[i]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
        if temp_buckets == buckets:
            actions = temp_actions
            break
    return actions

jugs = [33, 87, 48, 30, 61, 60]
buckets = [170, 225, 238, 317]

solution = pour_water(jugs, buckets)
print(solution)
