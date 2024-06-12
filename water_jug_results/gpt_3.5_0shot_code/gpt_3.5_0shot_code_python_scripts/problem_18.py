
from itertools import permutations

def pour_water(jug, bucket, actions):
    if jug[1] + bucket[1] <= bucket[0]:
        new_jug = (jug[0], jug[1] + bucket[1])
        new_bucket = (bucket[0], 0)
    else:
        new_jug = (jug[0], jug[1] - (bucket[0] - bucket[1]))
        new_bucket = (bucket[0], bucket[0])
    actions.append(('pour', jug[0], bucket[0]))
    return new_jug, new_bucket, actions

def solve_water_jug_problem(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        jugs_state = [(jug, 0) for jug in perm]
        buckets_state = [(bucket, 0) for bucket in buckets]
        for i in range(len(jugs_state)):
            jugs_state[i], buckets_state[i], actions = pour_water(jugs_state[i], buckets_state[i], actions)
        if all(bucket[1] == bucket[0] for bucket in buckets_state):
            return actions
    return None

jugs = [(71, 0), (124, 0), (95, 0), (42, 0), (56, 0), (41, 0)]
buckets = [(291, 0), (292, 0), (326, 0)]

solution = solve_water_jug_problem(jugs, buckets)
print(solution)
