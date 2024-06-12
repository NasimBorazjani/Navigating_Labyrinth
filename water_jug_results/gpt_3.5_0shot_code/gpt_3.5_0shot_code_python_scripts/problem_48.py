
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
    if action[0] == '+':
        new_state[action[2]-1] += action[1]
    elif action[0] == '-':
        new_state[action[2]-1] -= action[1]
    return tuple(new_state)

# Function to solve the problem using depth-first search
def solve(jugs, buckets, target):
    actions = generate_actions(jugs, buckets)
    for perm in permutations(actions, len(jugs)*len(buckets)):
        state = (0, 0, 0)
        path = []
        for action in perm:
            new_state = apply_action(state, action)
            if is_valid(new_state):
                state = new_state
                path.append(action)
                if state == target:
                    return path
    return None

# Given data
jugs = [121, 87, 150, 52, 43, 139, 90, 44, 59, 146]
buckets = [1, 2, 3]
target = (249, 446, 530)

# Solve the problem
solution = solve(jugs, buckets, target)

# Print the solution
print(solution)
