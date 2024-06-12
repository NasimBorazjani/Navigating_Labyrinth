
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i, bucket in enumerate(temp_buckets):
                if bucket + jug <= buckets[i]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
                    if temp_buckets == buckets:
                        return temp_actions
    return None

jugs = [67, 55, 84, 148, 107, 114, 17, 143, 40, 39]
buckets = [192, 247, 479]

result = pour_water(jugs, buckets)
print(result)
