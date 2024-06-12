
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
        if temp_buckets == [357, 384, 522]:
            if not actions or len(temp_actions) < len(actions):
                actions = temp_actions
    return actions

jugs = {52: 0, 131: 1, 82: 2, 132: 3, 117: 4, 65: 5}
buckets = [0, 0, 0]

solution = fill_buckets(jugs, buckets)
print(solution)
