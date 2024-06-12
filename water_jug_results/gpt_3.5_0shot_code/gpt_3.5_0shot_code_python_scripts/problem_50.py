
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
        if temp_buckets == [263, 298, 505]:
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = {137, 147, 73, 131, 91, 94, 72, 31, 103, 78}
buckets = [0, 0, 0]

solution = fill_buckets(jugs, buckets)
print(solution)
