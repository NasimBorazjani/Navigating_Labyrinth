
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [117, 118, 23, 86, 109, 128, 104, 61]
buckets = [367, 390, 400, 470]

# Function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] > state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jug, bucket):
    actions = []
    if bucket + jug <= 470:
        actions.append(('+', jug, bucket))
    if bucket - jug >= 0:
        actions.append(('-', jug, bucket))
    return actions

# Function to perform an action
def perform_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += action[1]
    elif action[0] == '-':
        new_state[action[2]] -= action[1]
    return new_state

# Function to solve the problem using backtracking
def solve(state, actions):
    if len(actions) == 4:
        if state == buckets:
            return True
        else:
            return False
    
    for action in generate_actions(jugs[actions[-1]], state[-1]):
        new_state = perform_action(state, action)
        if is_valid(new_state):
            actions.append(action)
            if solve(new_state, actions):
                return True
            actions.pop()
    
    return False

# Find the shortest sequence of actions to fill the buckets
for perm in permutations(range(7)):
    if solve([0, 0, 0, 0], list(perm)):
        break

# Print the solution
print(list(actions))
