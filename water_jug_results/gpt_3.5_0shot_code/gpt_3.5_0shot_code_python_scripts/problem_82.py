
from itertools import permutations

# Function to check if the buckets are filled in ascending order
def check_buckets_filled(buckets):
    for i in range(len(buckets)-1):
        if buckets[i] >= buckets[i+1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jugs, buckets):
    actions = []
    for jug in jugs:
        for bucket_idx in range(len(buckets)):
            if buckets[bucket_idx] + jug <= buckets[bucket_idx+1]:
                actions.append(('+', jug, bucket_idx))
            if buckets[bucket_idx] - jug >= 0:
                actions.append(('-', jug, bucket_idx))
    return actions

# Function to simulate the actions and check if the buckets are filled
def simulate_actions(actions, jugs, buckets):
    for action in actions:
        if action[0] == '+':
            if buckets[action[2]] + action[1] <= buckets[action[2]+1]:
                buckets[action[2]] += action[1]
        elif action[0] == '-':
            if buckets[action[2]] - action[1] >= 0:
                buckets[action[2]] -= action[1]
        if check_buckets_filled(buckets):
            return True, actions
    return False, []

# Given jugs and buckets
jugs = [52, 55, 84, 135, 136, 47, 139, 76]
buckets = [0, 0, 0, 0, 292, 325, 496, 516]

# Generate all possible permutations of jugs
perms = permutations(jugs)

# Iterate through all permutations and simulate actions
for perm in perms:
    actions = generate_actions(perm, buckets)
    success, solution = simulate_actions(actions, perm, buckets)
    if success:
        print(solution)
        break
