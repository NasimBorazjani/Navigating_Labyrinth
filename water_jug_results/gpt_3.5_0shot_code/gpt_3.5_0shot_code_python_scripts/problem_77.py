
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [60, 59, 72, 93, 39, 74, 71, 84]
buckets = [166, 239, 286, 421]

# Define a function to check if a state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] < state[i-1]:
            return False
    return True

# Define a function to generate all possible actions
def generate_actions(jug):
    actions = []
    for i in range(4):
        actions.append(('+', jug, i+1))
        actions.append(('-', jug, i+1))
    return actions

# Define a function to apply an action to a state
def apply_action(state, action):
    op, jug, bucket = action
    new_state = list(state)
    if op == '+':
        new_state[bucket-1] += jug
    elif op == '-':
        new_state[bucket-1] -= jug
    return tuple(new_state)

# Define a function to solve the problem using depth-first search
def solve():
    stack = [(tuple([0]*4), [])]
    while stack:
        state, actions = stack.pop()
        if state == tuple(buckets):
            return actions
        for jug in jugs:
            for action in generate_actions(jug):
                new_state = apply_action(state, action)
                if is_valid(new_state):
                    stack.append((new_state, actions + [action]))

# Find the shortest sequence of actions to fill the buckets
solution = solve()
print(solution)
