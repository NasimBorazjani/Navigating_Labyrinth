
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

# Function to apply an action to a state
def apply_action(state, action):
    new_state = list(state)
    op, jug, bucket = action
    if op == '+':
        new_state[bucket-1] += jug
    elif op == '-':
        new_state[bucket-1] -= jug
    return tuple(new_state)

# Function to solve the problem using depth-first search
def solve(jugs, buckets, target):
    actions = generate_actions(jugs, buckets)
    for perm in permutations(actions, len(jugs)*len(buckets)):
        state = (0, 0, 0, 0)
        solution = []
        for action in perm:
            new_state = apply_action(state, action)
            if is_valid(new_state):
                state = new_state
                solution.append(action)
                if state == target:
                    return solution
    return None

# Given data
jugs = [58, 18, 19, 47, 86, 75, 119, 34]
buckets = [234, 331, 343, 379]
target = (234, 331, 343, 379)

# Solve the problem
solution = solve(jugs, buckets, target)
print(solution)
