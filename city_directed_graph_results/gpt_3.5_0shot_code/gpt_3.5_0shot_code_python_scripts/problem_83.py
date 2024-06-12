
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
]

# Define the cities
cities = ['J', 'H', 'X', 'L', 'F', 'A', 'P', 'M', 'D', 'R', 'T', 'Z', 'N', 'K']

# Define the starting city
start_city = 'X'

# Find all possible paths that visit N and K twice
all_paths = []
for path in itertools.permutations(cities[1:], 12):
    path = [start_city] + list(path) + [start_city]
    if path.count('N') == 2 and path.count('K') == 2:
        all_paths.append(path)

# Calculate the travel time for each path
min_time = float('inf')
quickest_path = None
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        from_city = cities.index(path[i])
        to_city = cities.index(path[i + 1])
        time += adjacency_matrix[from_city][to_city]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
