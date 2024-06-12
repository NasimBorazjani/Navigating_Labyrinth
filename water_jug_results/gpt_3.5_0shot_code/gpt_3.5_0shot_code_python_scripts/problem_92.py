
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the buckets
jugs = [143, 34, 117, 130, 50, 142, 144, 150, 29, 78]
buckets = [307, 316, 325, 622]

# Function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] > state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jug, bucket):
    actions = []
    if bucket + jug <= 622:
        actions.append(('+', jug, bucket))
    if bucket - jug >= 0:
        actions.append(('-', jug, bucket))
    return actions

# Function to apply an action to a state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += action[1]
    elif action[0] == '-':
        new_state[action[2]] -= action[1]
    return new_state

# Generate all possible permutations of jugs
jug_permutations = permutations(jugs, 4)

# Iterate through all permutations to find a valid solution
for perm in jug_permutations:
    state = [0, 0, 0, 0]
    actions = []
    for jug in perm:
        for i in range(4):
            possible_actions = generate_actions(jug, state[i])
            for action in possible_actions:
                new_state = apply_action(state, action)
                if is_valid(new_state):
                    state = new_state
                    actions.append(action)
                    break
    if state == buckets:
        break

# Print the solution
print(actions)
