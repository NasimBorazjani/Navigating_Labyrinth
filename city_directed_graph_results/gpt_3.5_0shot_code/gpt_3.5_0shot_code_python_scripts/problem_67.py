
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
]

# Define the cities
cities = ['A', 'K', 'G', 'U', 'Q', 'D', 'N', 'X', 'S', 'V', 'Y', 'R', 'Z']

# Define the starting city
start_city = 'S'

# Find all possible paths from S to N to R and back to S
all_paths = []
for path in itertools.permutations(['N', 'R']):
    for perm in itertools.permutations(cities):
        if perm[0] == start_city:
            full_path = [start_city] + list(perm) + list(path) + [start_city]
            all_paths.append(full_path)

# Calculate the total travel time for each path
min_time = float('inf')
quickest_path = None
for path in all_paths:
    total_time = 0
    for i in range(len(path) - 1):
        from_city = cities.index(path[i])
        to_city = cities.index(path[i + 1])
        total_time += adjacency_matrix[from_city][to_city]
    if total_time < min_time:
        min_time = total_time
        quickest_path = path

print(quickest_path)
