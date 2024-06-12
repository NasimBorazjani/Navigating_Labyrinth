
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
    stack = [(tuple([0]*len(buckets)), [])]
    
    while stack:
        state, path = stack.pop()
        
        if state == target:
            return path
        
        for action in actions:
            new_state = apply_action(state, action)
            if is_valid(new_state):
                stack.append((new_state, path + [action]))

# Given data
jugs = [19, 42, 18, 127, 106, 32, 22, 137]
buckets = [245, 252, 264, 314]

# Target state
target = tuple(buckets)

# Solve the problem
solution = solve(jugs, buckets, target)

# Print the solution
print(solution)
