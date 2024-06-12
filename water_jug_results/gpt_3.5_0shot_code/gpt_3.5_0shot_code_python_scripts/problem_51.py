
from itertools import permutations

def fill_buckets(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(3):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_buckets[i] += jug
                    temp_actions.append(('+', jug, i+1))
        if temp_buckets == [454, 547, 601]:
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = {51: 0, 129: 1, 150: 2, 138: 3, 128: 4, 72: 5, 69: 6, 111: 7, 75: 8}
buckets = [0, 0, 0]

solution = fill_buckets(jugs, buckets)
print(solution)
