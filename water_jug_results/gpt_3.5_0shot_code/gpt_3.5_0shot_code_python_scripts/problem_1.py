
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
                    if temp_buckets == [274, 297, 343]:
                        return temp_actions
    return None

jugs = {41: 0, 26: 1, 44: 2, 75: 3, 40: 4, 136: 5}
buckets = [0, 0, 0]

result = pour_water(jugs, buckets)
print(result)
