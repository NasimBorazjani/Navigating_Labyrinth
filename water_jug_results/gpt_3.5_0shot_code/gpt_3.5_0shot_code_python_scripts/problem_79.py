
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [99, 47, 122, 123, 72, 136, 51, 71]
buckets = [274, 292, 361, 438]

# Function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] < state[i-1]:
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

# Function to perform the actions and update the state
def perform_action(state, action):
    op, amount, bucket = action
    new_state = list(state)
    if op == '+':
        new_state[bucket] += amount
    elif op == '-':
        new_state[bucket] -= amount
    return new_state

# Function to solve the problem using depth-first search
def solve():
    for perm in permutations(jugs):
        state = [0, 0, 0, 0]
        actions = []
        stack = [(state, actions)]
        
        while stack:
            current_state, current_actions = stack.pop()
            
            if current_state == buckets:
                return current_actions
            
            if not is_valid(current_state):
                continue
            
            possible_actions = generate_actions(current_state)
            
            for action in possible_actions:
                new_state = perform_action(current_state, action)
                new_actions = list(current_actions)
                new_actions.append(action)
                stack.append((new_state, new_actions))

# Solve the problem and print the solution
solution = solve()
print(solution)
