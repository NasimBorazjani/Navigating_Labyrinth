
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]

# Define the cities
cities = ['J', 'H', 'K', 'W', 'X', 'I', 'B', 'U', 'D', 'Z', 'G']

# Find all possible paths from city D to Z and H
all_paths = []
for path in itertools.permutations([9, 10], 2):
    all_paths.append(['D'] + [cities[i] for i in path] + ['D'])

# Calculate the total travel time for each path
total_times = []
for path in all_paths:
    total_time = 0
    for i in range(len(path) - 1):
        total_time += adjacency_matrix[cities.index(path[i])][cities.index(path[i+1])]
    total_times.append(total_time)

# Find the quickest path
quickest_path_index = total_times.index(min(total_times))
quickest_path = all_paths[quickest_path_index]

print(quickest_path)
