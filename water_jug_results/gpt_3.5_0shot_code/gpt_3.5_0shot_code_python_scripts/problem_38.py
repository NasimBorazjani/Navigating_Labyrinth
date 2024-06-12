
from itertools import permutations

def pour_water(jugs, target):
    for perm in permutations(jugs):
        buckets = [0, 0, 0]
        actions = []
        for jug in perm:
            for i in range(3):
                if buckets[i] + jug <= target[i]:
                    buckets[i] += jug
                    actions.append(('+', jug, i+1))
                    break
        if buckets == target:
            return actions

jugs = [117, 128, 36, 129, 103, 53, 21, 119, 105, 26]
target = [394, 425, 426]

actions = pour_water(jugs, target)
print(actions)
