
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(3):
                if temp_buckets[i] + jug <= buckets[i] and (i == 2 or temp_buckets[i] + jug <= temp_buckets[i+1]):
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
                    if temp_buckets == buckets:
                        return temp_actions
    return None

jugs = [15, 138, 24, 10, 30, 82, 11, 94]
buckets = [239, 275, 286]

result = pour_water(jugs, buckets)
print(result)
