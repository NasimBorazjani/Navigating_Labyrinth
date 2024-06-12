
from itertools import permutations

# Function to check if the buckets are filled as specified
def check_buckets_filled(buckets):
    return buckets[0] == 191 and buckets[1] == 269 and buckets[2] == 328

# Function to perform the actions on the buckets
def perform_action(action, buckets, jugs):
    if action[0] == '+':
        jug_idx = jugs.index(action[1])
        if buckets[action[2]-1] + jugs[jug_idx] <= buckets[action[2]]:
            buckets[action[2]-1] += jugs[jug_idx]
            return True
    elif action[0] == '-':
        jug_idx = jugs.index(action[1])
        if buckets[action[2]-1] - jugs[jug_idx] >= 0:
            buckets[action[2]-1] -= jugs[jug_idx]
            return True
    return False

# Given jugs and buckets
jugs = [76, 63, 111, 59, 11, 108, 16, 66, 75, 67]
buckets = [0, 0, 0]

# Generate all possible permutations of jugs
perm_jugs = permutations(jugs, 3)

# Try each permutation to find the shortest sequence of actions
for perm in perm_jugs:
    actions = []
    buckets = [0, 0, 0]
    for jug in perm:
        for i in range(3):
            if perform_action(('+', jug, i+1), buckets, jugs):
                actions.append(('+', jug, i+1))
                if check_buckets_filled(buckets):
                    print(actions)
                    exit()
            if perform_action(('-', jug, i+1), buckets, jugs):
                actions.append(('-', jug, i+1))
                if check_buckets_filled(buckets):
                    print(actions)
                    exit()
