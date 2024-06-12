
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [150, 84, 29, 140, 98, 83, 32]
buckets = [243, 250, 446]

# Define a function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Define a function to generate all possible actions
def generate_actions(state):
    actions = []
    for jug in jugs:
        for i in range(3):
            if state[i] + jug <= buckets[i]:
                actions.append(('+', jug, i))
            if state[i] - jug >= 0:
                actions.append(('-', jug, i))
    return actions

# Define a function to apply an action to a state
def apply_action(state, action):
    op, jug, bucket = action
    new_state = list(state)
    if op == '+':
        new_state[bucket] += jug
    elif op == '-':
        new_state[bucket] -= jug
    return tuple(new_state)

# Define a function to solve the problem using breadth-first search
def solve():
    queue = [(0, (0, 0, 0), [])]
    visited = set()
    
    while queue:
        cost, state, actions = queue.pop(0)
        
        if state == tuple(buckets):
            return actions
        
        if state not in visited and is_valid(state):
            visited.add(state)
            for action in generate_actions(state):
                new_state = apply_action(state, action)
                new_actions = actions + [action]
                queue.append((cost + 1, new_state, new_actions))
    
    return None

# Find the shortest sequence of actions to fill the buckets
solution = solve()
print(solution)
