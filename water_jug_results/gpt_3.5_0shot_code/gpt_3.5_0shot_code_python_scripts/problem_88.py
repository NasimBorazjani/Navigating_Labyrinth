
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [95, 111, 144, 57, 13, 58, 12]
buckets = [226, 271, 331, 394]

# Function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] > state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(state):
    actions = []
    for i in range(len(jugs)):
        for j in range(len(state)):
            if state[j] + jugs[i] <= buckets[j]:
                actions.append(('+', jugs[i], j))
            if state[j] - jugs[i] >= 0:
                actions.append(('-', jugs[i], j))
    return actions

# Function to perform an action on a state
def perform_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += action[1]
    elif action[0] == '-':
        new_state[action[2]] -= action[1]
    return new_state

# Function to solve the problem using depth-first search
def solve():
    stack = [([0, 0, 0, 0], [])]
    
    while stack:
        state, actions = stack.pop()
        
        if state == buckets:
            return actions
        
        if not is_valid(state):
            continue
        
        possible_actions = generate_actions(state)
        
        for action in possible_actions:
            new_state = perform_action(state, action)
            new_actions = actions + [action]
            stack.append((new_state, new_actions))

# Find the shortest sequence of actions to fill the buckets
solution = solve()
print(solution)
