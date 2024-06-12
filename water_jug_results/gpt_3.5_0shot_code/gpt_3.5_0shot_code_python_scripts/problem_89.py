
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [30, 26, 116, 76, 98, 48, 46, 45]
buckets = [201, 269, 315, 333]

# Function to check if a state is valid
def is_valid(state):
    for i in range(len(state) - 1):
        if state[i] > state[i + 1]:
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

# Function to apply an action to a state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += action[1]
    elif action[0] == '-':
        new_state[action[2]] -= action[1]
    return tuple(new_state)

# Breadth-first search to find the shortest sequence of actions
def bfs():
    queue = [(0, (0, 0, 0, 0), [])]
    visited = set()
    
    while queue:
        cost, state, actions = queue.pop(0)
        
        if state == (201, 269, 315, 333):
            return actions
        
        if state not in visited:
            visited.add(state)
            if is_valid(state):
                possible_actions = generate_actions(state)
                for action in possible_actions:
                    new_state = apply_action(state, action)
                    new_actions = actions + [action]
                    queue.append((cost + 1, new_state, new_actions))
    
    return None

# Find the shortest sequence of actions
solution = bfs()
print(solution)
