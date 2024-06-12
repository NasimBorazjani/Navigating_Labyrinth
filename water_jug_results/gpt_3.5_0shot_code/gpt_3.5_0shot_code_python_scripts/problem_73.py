
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [56, 81, 132, 41, 86, 128, 57, 138]
buckets = [232, 401, 444, 451]

# Define a function to generate all possible actions for filling or emptying a bucket
def generate_actions(jug, bucket):
    actions = []
    if bucket + jug <= 451:
        actions.append(('+', jug, bucket))
    if bucket - jug >= 0:
        actions.append(('-', jug, bucket))
    return actions

# Define a function to check if a sequence of actions is valid
def is_valid(actions):
    buckets = [0, 0, 0, 0]
    for action in actions:
        if action[0] == '+':
            buckets[action[2]-1] += action[1]
        else:
            buckets[action[2]-1] -= action[1]
        if any(buckets[i] < 0 for i in range(4)):
            return False
        if any(buckets[i] > buckets[i+1] for i in range(3)):
            return False
    return True

# Generate all possible sequences of actions
actions_permutations = permutations([(jug, bucket) for jug in jugs for bucket in range(1, 5)], 8)

# Find the shortest valid sequence of actions
for actions in actions_permutations:
    if is_valid(actions):
        print(list(actions))
        break
