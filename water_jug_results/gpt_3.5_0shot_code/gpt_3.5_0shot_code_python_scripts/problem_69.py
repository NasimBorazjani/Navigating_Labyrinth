
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
                    if temp_buckets == [257, 260, 269, 291]:
                        return temp_actions
        actions.append(temp_actions)

    min_actions = min(actions, key=len)
    return min_actions

jugs = {34: 0, 98: 1, 27: 2, 19: 3, 52: 4, 53: 5}
buckets = [257, 260, 269, 291]

result = pour_water(jugs, buckets)
print(result)
