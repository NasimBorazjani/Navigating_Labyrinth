
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [14, 46, 13, 110, 38, 21, 45, 130]
targets = [215, 219, 262]

# Define a function to generate all possible actions for filling or emptying a jug
def generate_actions(jug_capacity):
    actions = []
    actions.extend([('+', jug_capacity, i) for i in range(1, 4)]
    actions.extend(('-', jug_capacity, i) for i in range(1, 4))
    return actions

# Define a function to check if a state is valid
def is_valid(state):
    for i in range(2):
        if state[i] > state[i+1]:
            return False
    return True

# Define a function to perform the actions and update the state
def perform_action(state, action):
    op, jug_capacity, bucket_num = action
    if op == '+':
        state[bucket_num-1] += jug_capacity
    elif op == '-':
        state[bucket_num-1] -= jug_capacity
    return state

# Define a function to find the shortest sequence of actions to fill the buckets
def find_shortest_sequence(jugs, targets):
    actions = []
    min_sequence = None
    min_length = float('inf')
    
    for perm in permutations(jugs):
        state = [0, 0, 0]
        sequence = []
        
        for jug_capacity in perm:
            for action in generate_actions(jug_capacity):
                new_state = perform_action(state.copy(), action)
                if is_valid(new_state):
                    state = new_state
                    sequence.append(action)
                    
                    if state == targets:
                        if len(sequence) < min_length:
                            min_length = len(sequence)
                            min_sequence = sequence.copy()
        
        actions.append(sequence)
    
    return min_sequence

# Find the shortest sequence of actions to fill the buckets
shortest_sequence = find_shortest_sequence(jugs, targets)

# Print the solution as a list of action tuples in Python syntax
print(shortest_sequence)
