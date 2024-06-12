
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
                    if check_solution(temp_buckets):
                        return temp_actions
        actions.append(temp_actions)
    return min(actions, key=len)

def check_solution(buckets):
    return buckets[0] == 170 and buckets[1] == 385 and buckets[2] == 499

jugs = {80, 69, 12, 52, 107, 53, 82, 95, 108}
buckets = [0, 0, 0]

solution = pour_water(jugs, buckets)
print(solution)
