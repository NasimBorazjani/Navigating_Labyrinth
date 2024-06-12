
from itertools import permutations

# Define the capacities of the jugs and the target amounts for the unlabeled buckets
jugs = [137, 100, 82, 25, 21, 101, 118, 117, 26, 131]
buckets = [272, 439, 458, 590]

# Function to generate all possible actions
def generate_actions(jug, bucket):
    actions = []
    if bucket + jug <= 590:
        actions.append(('+', jug, bucket))
    if bucket - jug >= 0:
        actions.append(('-', jug, bucket))
    return actions

# Function to perform the actions and update the state of the buckets
def perform_action(action, state):
    if action[0] == '+':
        state[action[2]] += action[1]
    elif action[0] == '-':
        state[action[2]] -= action[1]
    return state

# Function to check if the state of the buckets matches the target
def check_target(state):
    return state == [272, 439, 458, 590]

# Function to find the shortest sequence of actions to fill the buckets
def find_solution(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        state = [0, 0, 0, 0]
        temp_actions = []
        for jug in perm:
            for i in range(4):
                possible_actions = generate_actions(jug, state[i])
                for action in possible_actions:
                    temp_state = state.copy()
                    temp_state = perform_action(action, temp_state)
                    if check_target(temp_state):
                        temp_actions.append(action)
                        actions = temp_actions
                        return actions
                    elif all(temp_state[j] <= temp_state[j+1] for j in range(3)):
                        temp_actions.append(action)
                        state = temp_state
                        break
    return actions

# Find the shortest sequence of actions to fill the buckets
solution = find_solution(jugs, buckets)
print(solution)
