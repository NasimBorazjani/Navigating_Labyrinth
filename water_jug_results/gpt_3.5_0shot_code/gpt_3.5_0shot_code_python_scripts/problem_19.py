
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [21, 62, 98, 143, 61, 110, 140, 40]
buckets = [280, 338, 353]

# Generate all possible permutations of the jugs
perms = permutations(jugs)

# Function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Function to perform the actions
def perform_action(state, action):
    op, jug, bucket = action
    if op == '+':
        amount = min(jug, buckets[bucket] - state[bucket])
        state[bucket] += amount
        state[jug] -= amount
    elif op == '-':
        amount = min(jug, state[bucket])
        state[bucket] -= amount
        state[jug] += amount
    return state

# Function to find the shortest sequence of actions
def find_shortest_sequence():
    for perm in perms:
        state = [0, 0, 0]
        actions = []
        for jug in perm:
            for bucket in range(3):
                if state[bucket] < buckets[bucket]:
                    actions.append(('+', jug, bucket))
                    state = perform_action(state, ('+', jug, bucket))
                    if not is_valid(state):
                        break
            if state == buckets:
                return actions
    return None

# Find the shortest sequence of actions
shortest_sequence = find_shortest_sequence()

# Print the solution
print(shortest_sequence)
