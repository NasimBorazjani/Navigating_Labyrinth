
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
                    break
                elif temp_buckets[i] - jug >= 0 and (i == 0 or temp_buckets[i] - jug >= temp_buckets[i-1]):
                    temp_buckets[i] -= jug
                    temp_actions.append(('-', jug, i+1))
                    break
    return None

jugs = [75, 20, 64, 106, 88, 13, 107, 131]
buckets = [287, 394, 455]

result = pour_water(jugs, buckets)
print(result)
