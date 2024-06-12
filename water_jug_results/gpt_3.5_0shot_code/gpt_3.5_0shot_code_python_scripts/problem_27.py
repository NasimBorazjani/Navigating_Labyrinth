
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
            actions = temp_actions
            break
    return actions

jugs = [80, 76, 132, 60, 83, 28, 75, 26]
buckets = [337, 378, 398]

solution = pour_water(jugs, buckets)
print(solution)
