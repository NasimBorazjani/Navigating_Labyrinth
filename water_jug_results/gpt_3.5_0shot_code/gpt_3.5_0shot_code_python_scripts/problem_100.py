
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [126, 120, 127, 110, 54, 39, 38, 47, 139, 99]
buckets = [219, 240, 312, 411]

# Function to check if a state is valid
def is_valid(state):
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jug):
    actions = []
    for bucket in range(1, 5):
        actions.append(('+', jug, bucket))
        actions.append(('-', jug, bucket))
    return actions

# Function to apply an action to a state
def apply_action(state, action):
    new_state = state.copy()
    if action[0] == '+':
        new_state[action[2]-1] += action[1]
    elif action[0] == '-':
        new_state[action[2]-1] -= action[1]
    return new_state

# Function to solve the problem using backtracking
def solve(state, actions):
    if len(state) == 4:
        if state == buckets:
            return True
        return False
    
    for action in actions:
        new_state = apply_action(state, action)
        if is_valid(new_state):
            if solve(new_state, actions):
                solution.append(action)
                return True
    return False

# Generate all possible actions
all_actions = []
for jug in jugs:
    all_actions.extend(generate_actions(jug))

# Try all permutations of the jugs to find the shortest sequence of actions
solution = []
for perm in permutations(jugs):
    if solve([0, 0, 0, 0], all_actions):
        break

# Print the solution
print(solution)
