
from itertools import permutations

# Function to check if the buckets are filled as required
def check_buckets_filled(buckets):
    return buckets[0] == 287 and buckets[1] == 423 and buckets[2] == 583

# Function to perform the pour action
def pour(bucket, jug):
    pour_amount = min(jug, bucket[1] - bucket[0])
    bucket[0] += pour_amount
    return pour_amount

# Function to solve the water jug problem
def solve_water_jug_problem(jugs, buckets):
    actions = []
    for perm in permutations(jugs):
        temp_buckets = [list(bucket) for bucket in buckets]
        temp_actions = []
        for jug in perm:
            for i, bucket in enumerate(temp_buckets):
                pour_amount = pour(bucket, jug)
                temp_actions.append(('+', jug, i+1))
                if check_buckets_filled(temp_buckets):
                    return temp_actions
    return None

# Given jugs and buckets
jugs = [20, 142, 147, 48, 29, 113, 17, 18, 112, 68]
buckets = [[0, 287], [0, 423], [0, 583]]

# Solve the water jug problem
solution = solve_water_jug_problem(jugs, buckets)

# Print the solution
print(solution)
