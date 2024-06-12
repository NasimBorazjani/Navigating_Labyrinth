
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
                    break
                elif temp_buckets[i] - jug >= 0 and (i == 0 or temp_buckets[i] - jug >= temp_buckets[i-1]):
                    temp_buckets[i] -= jug
                    temp_actions.append(('-', jug, i+1))
                    break
        if temp_buckets == buckets:
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = [59, 68, 104, 106, 69, 42]
buckets = [196, 210, 238]

solution = pour_water(jugs, buckets)
print(solution)
