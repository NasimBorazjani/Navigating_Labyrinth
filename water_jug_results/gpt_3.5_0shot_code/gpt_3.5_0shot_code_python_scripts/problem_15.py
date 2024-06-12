
from itertools import permutations

def pour_water(jug, bucket, action):
    if action[0] == '+':
        return min(jug, bucket + action[1]), max(0, bucket + action[1])
    elif action[0] == '-':
        return min(jug, bucket), max(0, bucket - action[1])

def is_valid_state(state):
    return state[0] <= state[1] <= state[2]

def solve_water_jug_problem(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        state = [0, 0, 0]
        for jug in perm:
            for i in range(3):
                state[i], buckets[i] = pour_water(jug, buckets[i], ('+', jug, i+1))
                actions.append(('+', jug, i+1))
                if is_valid_state(buckets):
                    return actions
    return None

jugs = [19, 50, 12, 63, 143, 13]
buckets = [160, 170, 330]

solution = solve_water_jug_problem(jugs, buckets)
print(solution)
