
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(3):
                if temp_buckets[i] + jug <= buckets[i] and temp_buckets[i] + jug <= temp_buckets[i+1]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
        if temp_buckets == buckets:
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = [118, 15, 88, 145, 84, 14, 107, 31]
buckets = [226, 258, 296]

solution = pour_water(jugs, buckets)
print(solution)
