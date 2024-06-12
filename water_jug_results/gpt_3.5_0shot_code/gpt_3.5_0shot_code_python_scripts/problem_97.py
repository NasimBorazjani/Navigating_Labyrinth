
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [59, 104, 79, 23, 20, 60, 14, 15, 119, 105]
buckets = [215, 403, 420, 504]

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

# Function to perform the actions and update the state
def perform_action(state, action):
    op, amount, bucket = action
    new_state = list(state)
    if op == '+':
        new_state[bucket] += amount
    elif op == '-':
        new_state[bucket] -= amount
    return new_state

# Function to find the shortest sequence of actions to fill the buckets
def find_solution():
    for perm in permutations(jugs):
        state = [0, 0, 0, 0]
        actions = []
        for jug in perm:
            actions.extend(generate_actions(state))
            for action in actions:
                new_state = perform_action(state, action)
                if is_valid(new_state):
                    state = new_state
                    actions.remove(action)
                    break
        if state == buckets:
            return actions

# Find the shortest sequence of actions to fill the buckets
solution = find_solution()
print(solution)
