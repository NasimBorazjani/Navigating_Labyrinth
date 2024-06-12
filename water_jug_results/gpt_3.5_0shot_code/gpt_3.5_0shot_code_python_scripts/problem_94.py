
from itertools import permutations

# Define the capacities of the water jugs and the target amounts for the unlabeled buckets
jugs = [81, 56, 41, 88, 137, 14, 149, 120, 87, 104]
buckets = [377, 456, 512, 541]

# Generate all possible permutations of the jugs
perm = permutations(jugs, len(buckets))

# Function to check if a bucket is filled to its target amount
def is_filled(bucket, target):
    return bucket == target

# Function to simulate the pouring of water from a jug to a bucket
def pour_water(jug, bucket, target):
    if jug >= target - bucket:
        return target, jug - (target - bucket)
    else:
        return bucket + jug, 0

# Function to solve the problem
def solve():
    for p in perm:
        actions = []
        buckets_state = [0, 0, 0, 0]
        jugs_state = list(p)
        
        for i in range(len(buckets)):
            while not is_filled(buckets_state[i], buckets[i]):
                for j in range(len(jugs_state)):
                    if jugs_state[j] > 0:
                        buckets_state[i], jugs_state[j] = pour_water(jugs_state[j], buckets_state[i], buckets[i])
                        actions.append(('+', jugs_state[j], i+1))
                        if is_filled(buckets_state[i], buckets[i]):
                            break
                        actions.append(('-', jugs_state[j], i+1))
        
        if all(is_filled(buckets_state[i], buckets[i]) for i in range(len(buckets))):
            return actions

# Print the solution
solution = solve()
print(solution)
