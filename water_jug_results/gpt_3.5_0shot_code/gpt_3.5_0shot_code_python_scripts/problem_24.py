
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
    return buckets[0] == 168 and buckets[1] == 239 and buckets[2] == 307

jugs = {33: 0, 56: 1, 108: 2, 53: 3, 65: 4, 54: 5, 52: 6, 59: 7}
buckets = [0, 0, 0]

solution = pour_water(jugs, buckets)
print(solution)
