
from itertools import permutations

# Function to check if the buckets are filled as required
def check_buckets(buckets):
    return buckets[0] == 342 and buckets[1] == 373 and buckets[2] == 447

# Function to perform the actions
def perform_action(action, buckets, jugs):
    if action[0] == '+':
        amount = min(jugs[action[1]], buckets[action[2]])
        buckets[action[2]] -= amount
        buckets[(action[2] + 1) % 3] += amount
    elif action[0] == '-':
        amount = min(jugs[action[1]], 447 - buckets[action[2]])
        buckets[action[2]] += amount
        buckets[(action[2] + 1) % 3] -= amount

# Given jugs and buckets
jugs = [104, 14, 83, 46, 128, 34, 137, 15, 19, 126]
buckets = [0, 0, 0]

# Generate all possible permutations of jugs
perms = permutations(range(10), 3)

# Try each permutation to find the shortest sequence of actions
min_actions = float('inf')
min_action_sequence = []

for perm in perms:
    actions = []
    temp_buckets = buckets.copy()
    
    for i in perm:
        while jugs[i] > 0:
            if temp_buckets[0] + jugs[i] <= 342:
                actions.append(('+', i, 0))
                perform_action(('+', i, 0), temp_buckets, jugs)
            elif temp_buckets[1] + jugs[i] <= 373:
                actions.append(('+', i, 1))
                perform_action(('+', i, 1), temp_buckets, jugs)
            elif temp_buckets[2] + jugs[i] <= 447:
                actions.append(('+', i, 2))
                perform_action(('+', i, 2), temp_buckets, jugs)
            else:
                break
        
        if check_buckets(temp_buckets):
            if len(actions) < min_actions:
                min_actions = len(actions)
                min_action_sequence = actions.copy()
            break

        while temp_buckets[0] > 0:
            if temp_buckets[0] - jugs[i] >= 0:
                actions.append(('-', i, 0))
                perform_action(('-', i, 0), temp_buckets, jugs)
            elif temp_buckets[1] - jugs[i] >= 0:
                actions.append(('-', i, 1))
                perform_action(('-', i, 1), temp_buckets, jugs)
            elif temp_buckets[2] - jugs[i] >= 0:
                actions.append(('-', i, 2))
                perform_action(('-', i, 2), temp_buckets, jugs)
            else:
                break

# Print the shortest sequence of actions
print(min_action_sequence)
