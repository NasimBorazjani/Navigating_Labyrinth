
from itertools import permutations

# Function to check if the buckets are filled as specified
def check_buckets_filled(buckets):
    return buckets[0] == 258 and buckets[1] == 310 and buckets[2] == 514

# Function to perform the actions on the buckets
def perform_action(action, buckets, jugs):
    if action[0] == '+':
        if buckets[action[2]-1] + jugs[action[1]] <= buckets[action[2]]:
            buckets[action[2]-1] += jugs[action[1]]
        else:
            buckets[action[2]-1] = buckets[action[2]]
    elif action[0] == '-':
        if buckets[action[2]-1] - jugs[action[1]] >= 0:
            buckets[action[2]-1] -= jugs[action[1]]
        else:
            buckets[action[2]-1] = 0
    return buckets

# Given jugs and buckets
jugs = {62: 0, 144: 0, 80: 0, 72: 0, 100: 0, 127: 0, 18: 0, 82: 0, 42: 0, 99: 0}
buckets = [0, 0, 0]

# Generate all possible permutations of jugs
jug_permutations = permutations(jugs.keys())

# Try each permutation to find the shortest sequence of actions
shortest_sequence = None
min_actions = float('inf')

for perm in jug_permutations:
    buckets = [0, 0, 0]
    actions = []
    
    for jug in perm:
        for i in range(3):
            if buckets[i] + jugs[jug] <= buckets[i+1]:
                buckets[i] += jugs[jug]
                actions.append(('+', jug, i+1))
                break
            elif buckets[i] + jugs[jug] <= buckets[i]:
                buckets[i] += jugs[jug]
                actions.append(('+', jug, i))
                break
            elif i == 2:
                buckets[i] += jugs[jug]
                actions.append(('+', jug, i))
    
    if check_buckets_filled(buckets) and len(actions) < min_actions:
        shortest_sequence = actions
        min_actions = len(actions)

print(shortest_sequence)
