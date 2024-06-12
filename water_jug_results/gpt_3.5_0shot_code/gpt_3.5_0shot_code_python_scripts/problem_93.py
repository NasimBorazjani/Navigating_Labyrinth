
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [39, 110, 41, 54, 47, 33, 136, 40, 100]
buckets = [192, 459, 473, 493]

# Function to generate all possible actions for filling or emptying a bucket
def generate_actions(jug, bucket):
    actions = []
    if bucket < jug:
        actions.append(('-', jug, bucket))
    if bucket + jug <= 493:
        actions.append(('+', jug, bucket))
    return actions

# Function to check if a sequence of actions is valid
def is_valid(actions):
    buckets = [0, 0, 0, 0]
    for action in actions:
        if action[0] == '+':
            buckets[action[2]-1] += action[1]
        elif action[0] == '-':
            buckets[action[2]-1] -= action[1]
    return all(bucket >= 0 for bucket in buckets)

# Generate all possible permutations of jugs and buckets
perms = permutations(jugs, 4)

# Iterate through all permutations to find a valid sequence of actions
for perm in perms:
    actions = []
    for i in range(4):
        actions.extend(generate_actions(perm[i], buckets[i]))
        if not is_valid(actions):
            break
    if is_valid(actions):
        print(actions)
        break
