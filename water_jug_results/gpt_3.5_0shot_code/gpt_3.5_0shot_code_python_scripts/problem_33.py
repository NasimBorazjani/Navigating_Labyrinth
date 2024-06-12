
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
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = [146, 57, 69, 52, 132, 80, 145]
buckets = [456, 538, 549]

result = pour_water(jugs, buckets)
print(result)
