
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
        for bucket in buckets:
            actions.append(('+', jug, bucket))
            actions.append(('-', jug, bucket))
    return actions

# Function to apply an action to the current state
def apply_action(state, action):
    op, jug, bucket = action
    if op == '+':
        state[bucket] += jug
    elif op == '-':
        state[bucket] -= jug
    return state

# Function to solve the problem
def solve(jugs, buckets):
    actions = generate_actions(jugs, buckets)
    shortest_sequence = None
    shortest_length = float('inf')

    for perm in permutations(actions, len(buckets)):
        state = [0] * len(buckets)
        sequence = []
        valid = True

        for action in perm:
            state = apply_action(state, action)
            sequence.append(action)
            if not is_valid(state):
                valid = False
                break

        if valid and state == buckets and len(sequence) < shortest_length:
            shortest_sequence = sequence
            shortest_length = len(sequence)

    return shortest_sequence

# Given data
jugs = [123, 124, 133, 85, 74]
buckets = [276, 277, 355, 425]

# Solve the problem
solution = solve(jugs, buckets)
print(solution)
