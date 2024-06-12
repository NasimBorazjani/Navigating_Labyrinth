
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [116, 16, 79, 75, 30, 87, 28, 96, 15, 134]
buckets = [155, 208, 295]

# Function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(state):
    actions = []
    for jug in jugs:
        for i in range(3):
            if state[i] + jug <= buckets[i]:
                actions.append(('+', jug, i+1))
            if state[i] - jug >= 0:
                actions.append(('-', jug, i+1))
    return actions

# Function to perform the actions and update the state
def perform_action(state, action):
    action_type, jug, bucket = action
    new_state = list(state)
    if action_type == '+':
        new_state[bucket-1] += jug
    elif action_type == '-':
        new_state[bucket-1] -= jug
    return tuple(new_state)

# Breadth-first search to find the shortest sequence of actions
def bfs():
    queue = [(0, (0, 0, 0), [])]
    visited = set()
    
    while queue:
        steps, state, actions = queue.pop(0)
        
        if state == tuple(buckets):
            return actions
        
        if state not in visited and is_valid(state):
            visited.add(state)
            possible_actions = generate_actions(state)
            for action in possible_actions:
                new_state = perform_action(state, action)
                new_actions = actions + [action]
                queue.append((steps+1, new_state, new_actions))
    
    return None

# Find the shortest sequence of actions
solution = bfs()
print(solution)
