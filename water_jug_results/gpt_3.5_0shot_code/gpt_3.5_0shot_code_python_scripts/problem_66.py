
from itertools import permutations

def fill_buckets(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(len(temp_buckets)):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_actions.append(('+', jug, i+1))
                    temp_buckets[i] += jug
                    if temp_buckets == [270, 311, 372, 389]:
                        return temp_actions
    return None

jugs = {122: 0, 121: 1, 124: 2, 28: 3, 89: 4, 73: 5}
buckets = [0, 0, 0, 0]

solution = fill_buckets(jugs, buckets)
print(solution)
