
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [90, 21, 104, 111, 97, 22, 34, 15, 62, 52]
buckets = [177, 263, 294, 462]

# Function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] > state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jug, bucket):
    actions = []
    if bucket + jug <= 462:
        actions.append(('+', jug, bucket))
    if bucket - jug >= 0:
        actions.append(('-', jug, bucket))
    return actions

# Function to perform the actions and update the state
def perform_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += action[1]
    elif action[0] == '-':
        new_state[action[2]] -= action[1]
    return new_state

# Generate all possible permutations of jugs
jug_permutations = permutations(jugs, len(buckets))

# Iterate through all permutations to find the shortest sequence of actions
shortest_sequence = None
for perm in jug_permutations:
    state = [0, 0, 0, 0]
    actions = []
    for i in range(len(buckets)):
        while state[i] != buckets[i]:
            valid_actions = []
            for jug in perm:
                for j in range(i+1):
                    valid_actions.extend(generate_actions(jug, state[j]))
            for action in valid_actions:
                new_state = perform_action(state, action)
                if is_valid(new_state):
                    actions.append(action)
                    state = new_state
                    break
    if shortest_sequence is None or len(actions) < len(shortest_sequence):
        shortest_sequence = actions

# Print the shortest sequence of actions
print(shortest_sequence)
