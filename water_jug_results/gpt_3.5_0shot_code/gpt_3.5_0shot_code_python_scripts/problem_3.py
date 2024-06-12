
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        for i in range(3):
            bucket = buckets[i]
            current = [0, 0, 0]
            for jug in perm:
                if jug >= bucket:
                    actions.append(('+', jug, i+1))
                    current[i] = jug
                    jug -= bucket
                    while jug > 0:
                        if jug >= buckets[i+1] - current[i+1]:
                            actions.append(('+', jug, i+2))
                            current[i+1] = buckets[i+1]
                            jug -= buckets[i+1] - current[i+1]
                        else:
                            actions.append(('+', jug, i+2))
                            current[i+1] += jug
                            jug = 0
                else:
                    actions.append(('+', jug, i+1))
                    current[i] = jug
        if current == buckets:
            return actions
        actions = []
    return None

jugs = [43, 149, 131, 132, 70, 104]
buckets = [284, 297, 436]

result = pour_water(jugs, buckets)
print(result)
