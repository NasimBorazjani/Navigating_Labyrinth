
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [82, 91, 135, 11, 12, 19, 143, 60]
buckets = [231, 288, 342, 410]

# Define a function to generate all possible actions for filling or emptying a bucket
def generate_actions(jug, bucket):
    actions = []
    if jug >= bucket:
        actions.append(('+', jug, bucket))
    if jug <= bucket:
        actions.append(('-', jug, bucket))
    return actions

# Define a function to check if a sequence of actions is valid
def is_valid(actions):
    buckets = [0, 0, 0, 0]
    for action in actions:
        if action[0] == '+':
            buckets[action[2]-1] += action[1]
        elif action[0] == '-':
            buckets[action[2]-1] -= action[1]
        if any(buckets[i] > buckets[i+1] for i in range(3)):
            return False
    return True

# Generate all possible permutations of actions
actions_permutations = permutations([(jug, bucket) for jug in jugs for bucket in range(1, 5)], len(jugs))

# Find the shortest sequence of valid actions
for actions in actions_permutations:
    if is_valid(actions):
        print(list(actions))
        break
