
from itertools import permutations

def pour_water(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = buckets.copy()
        temp_actions = []
        for jug in perm:
            for i in range(len(temp_buckets)):
                if temp_buckets[i] + jug <= jugs[jug]:
                    temp_actions.append(('+', jug, i+1))
                    temp_buckets[i] += jug
                    if check_valid(temp_buckets):
                        return temp_actions
        actions.append(temp_actions)
    return min(actions, key=len)

def check_valid(buckets):
    for i in range(len(buckets)-1):
        if buckets[i] > buckets[i+1]:
            return False
    return True

jugs = {87:0, 13:1, 27:2, 106:3, 18:4, 91:5, 17:6, 138:7}
buckets = [205, 365, 391, 414]

solution = pour_water(jugs, buckets)
print(solution)
