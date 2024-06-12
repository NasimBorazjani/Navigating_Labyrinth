
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [36, 72, 16, 80, 45, 67, 38, 32, 149, 37]
targets = [201, 202, 233]

# Function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(state, jug):
    actions = []
    for i in range(3):
        if state[i] < targets[i]:
            actions.append(('+', jug, i+1))
        if state[i] > 0:
            actions.append(('-', jug, i+1))
    return actions

# Function to perform an action and return the new state
def perform_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] += action[1]
    elif action[0] == '-':
        new_state[action[2]-1] -= action[1]
    return tuple(new_state)

# Function to solve the problem using depth-first search
def solve():
    for perm in permutations(jugs):
        stack = [(perm, [])]
        while stack:
            state, actions = stack.pop()
            if state == tuple(targets):
                return actions
            if is_valid(state):
                for jug in jugs:
                    for action in generate_actions(state, jug):
                        new_state = perform_action(state, action)
                        new_actions = actions + [action]
                        stack.append((new_state, new_actions))

# Solve the problem and print the solution
solution = solve()
print(solution)
