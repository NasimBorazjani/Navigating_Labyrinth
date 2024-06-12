
from itertools import permutations

def pour_water(jugs, target):
    actions = []
    for perm in permutations(jugs):
        buckets = [0, 0, 0]
        for jug in perm:
            for i in range(3):
                if buckets[i] + jug <= target[i]:
                    buckets[i] += jug
                    actions.append(('+', jug, i+1))
                    break
        if buckets == target:
            return actions

jugs = [22, 98, 38, 116, 140, 115, 21, 80, 92, 27]
target = [279, 488, 578]

result = pour_water(jugs, target)
print(result)
