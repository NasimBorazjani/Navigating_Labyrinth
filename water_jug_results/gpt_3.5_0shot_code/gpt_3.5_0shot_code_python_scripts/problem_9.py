
from itertools import permutations

# Function to check if the current state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] < state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jugs, buckets):
    actions = []
    for jug in jugs:
        for bucket in range(len(buckets)):
            if buckets[bucket] + jug <= jugs[jug]:
                actions.append(('+', jug, bucket))
            if buckets[bucket] - jug >= 0:
                actions.append(('-', jug, bucket))
    return actions

# Function to perform the actions and update the state
def perform_action(action, jugs, buckets):
    op, jug, bucket = action
    if op == '+':
        buckets[bucket] += jugs[jug]
    elif op == '-':
        buckets[bucket] -= jugs[jug]
    return buckets

# Function to solve the problem using backtracking
def solve(jugs, buckets, target, actions):
    if is_valid(buckets):
        if buckets == target:
            return actions
        for action in generate_actions(jugs, buckets):
            new_buckets = perform_action(action, jugs, buckets.copy())
            new_actions = actions.copy()
            new_actions.append(action)
            result = solve(jugs, new_buckets, target, new_actions)
            if result:
                return result
    return None

# Given jugs and target buckets
jugs = {129: 'A', 57: 'B', 45: 'C', 105: 'D', 128: 'E', 78: 'F'}
target_buckets = [344, 376, 386]

# Generate all permutations of jugs
perms = permutations(jugs.keys())

# Try each permutation to find the shortest sequence of actions
for perm in perms:
    jugs_perm = {key: jugs[key] for key in perm}
    actions = solve(jugs_perm, [0, 0, 0], target_buckets, [])
    if actions:
        print(actions)
        break
