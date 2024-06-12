
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [137, 29, 70, 138, 47, 64, 87, 16]
targets = [295, 327, 442]

# Function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(state):
    actions = []
    for i in range(len(jugs)):
        for j in range(3):
            if state[j] + jugs[i] <= targets[j]:
                actions.append(('+', jugs[i], j+1))
            if state[j] - jugs[i] >= 0:
                actions.append(('-', jugs[i], j+1))
    return actions

# Function to perform the actions and update the state
def perform_action(state, action):
    if action[0] == '+':
        state[action[2]-1] += action[1]
    elif action[0] == '-':
        state[action[2]-1] -= action[1]
    return state

# Function to solve the problem using depth-first search
def solve():
    stack = [([0, 0, 0], [])]
    
    while stack:
        state, actions = stack.pop()
        
        if state == targets:
            return actions
        
        if len(actions) >= 10:  # Limit the number of actions to prevent infinite loop
            continue
        
        if is_valid(state):
            possible_actions = generate_actions(state)
            for action in possible_actions:
                new_state = perform_action(state.copy(), action)
                new_actions = actions.copy()
                new_actions.append(action)
                stack.append((new_state, new_actions))

    return None

# Find the shortest sequence of actions to fill the buckets
solution = solve()
print(solution)
