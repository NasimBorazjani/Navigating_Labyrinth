
from itertools import permutations

# Function to check if a state is valid
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

# Function to apply an action to a state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] += action[1]
    elif action[0] == '-':
        new_state[action[2]-1] -= action[1]
    return tuple(new_state)

# Function to solve the problem
def solve(jugs, buckets, target):
    actions = generate_actions(jugs, buckets)
    shortest_sequence = None
    shortest_length = float('inf')

    for perm in permutations(jugs, len(buckets)):
        state = (0, 0, 0, 0)
        sequence = []

        for jug in perm:
            for action in actions:
                new_state = apply_action(state, action)
                if is_valid(new_state) and new_state[buckets.index(max(buckets))] == target[-1]:
                    sequence.append(action)
                    state = new_state
                    break

        if len(sequence) < shortest_length:
            shortest_length = len(sequence)
            shortest_sequence = sequence

    return shortest_sequence

# Given data
jugs = [141, 116, 66, 83, 142]
buckets = [397, 401, 419, 425]

# Solve the problem
solution = solve(jugs, buckets, buckets)
print(solution)
