
from itertools import permutations

# Function to check if the buckets are filled as required
def check_buckets(buckets):
    return buckets[0] == 254 and buckets[1] == 456 and buckets[2] == 579

# Function to perform the pouring action
def pour_water(jug, bucket):
    if jug + bucket <= bucket_capacities[bucket]:
        return jug, 0
    else:
        return jug - (bucket_capacities[bucket] - bucket), bucket_capacities[bucket]

# Given jug capacities
jug_capacities = [141, 101, 126, 26, 120, 75, 110, 108, 97, 100]

# Given bucket capacities
bucket_capacities = [254, 456, 579]

# Generate all permutations of jug capacities
jug_permutations = permutations(jug_capacities, 3)

# Iterate through all permutations to find the shortest sequence of actions
shortest_sequence = None
min_actions = float('inf')

for jugs in jug_permutations:
    buckets = [0, 0, 0]
    actions = []

    for jug in jugs:
        for i in range(3):
            if buckets[i] == bucket_capacities[i]:
                continue
            new_jug, new_bucket = pour_water(jug, buckets[i])
            actions.append(('+', jug, i+1))
            actions.append(('-', new_jug, i+1))
            buckets[i] = new_bucket

            if check_buckets(buckets):
                if len(actions) < min_actions:
                    min_actions = len(actions)
                    shortest_sequence = actions.copy()
                break

print(shortest_sequence)
