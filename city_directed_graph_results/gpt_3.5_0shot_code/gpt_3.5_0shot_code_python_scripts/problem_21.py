
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
]

# Define the cities
cities = ['I', 'K', 'D', 'M', 'Y', 'H', 'C', 'R', 'V', 'W', 'Q']

# Find all possible paths that visit I and Q exactly twice
all_paths = []
for path in itertools.permutations(cities[1:], len(cities)-1):
    path = ['Y'] + list(path) + ['Y']
    if path.count('I') == 2 and path.count('Q') == 2:
        all_paths.append(path)

# Calculate the travel time for each path
min_time = float('inf')
quickest_path = None
for path in all_paths:
    time = 0
    for i in range(len(path)-1):
        start = cities.index(path[i])
        end = cities.index(path[i+1])
        time += adjacency_matrix[start][end]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
