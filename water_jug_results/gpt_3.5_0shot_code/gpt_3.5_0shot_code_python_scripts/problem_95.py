
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [146, 45, 136, 13, 148, 17, 42, 137, 141, 31]
buckets = [307, 384, 555, 575]

# Function to check if a state is valid
def is_valid(state):
    for i in range(3):
        if state[i] > state[i+1]:
            return False
    return True

# Function to perform the actions and update the state
def perform_action(state, action):
    op, jug, bucket = action
    if op == '+':
        state[bucket-1] += jug
    elif op == '-':
        state[bucket-1] -= jug
    return state

# Generate all possible permutations of jugs and buckets
perms = permutations(jugs, 3)

# Iterate through each permutation and check if a valid solution exists
for perm in perms:
    state = [0, 0, 0, 0]
    actions = []
    for jug, bucket in zip(perm, buckets):
        while state[bucket-1] < bucket:
            if state[0] < bucket:
                state = perform_action(state, ('+', jug, 1))
                actions.append(('+', jug, 1))
            elif state[1] < bucket:
                state = perform_action(state, ('+', jug, 2))
                actions.append(('+', jug, 2))
            elif state[2] < bucket:
                state = perform_action(state, ('+', jug, 3))
                actions.append(('+', jug, 3))
            elif state[3] < bucket:
                state = perform_action(state, ('+', jug, 4))
                actions.append(('+', jug, 4))
        if not is_valid(state):
            break
    if is_valid(state):
        print(actions)
        break
