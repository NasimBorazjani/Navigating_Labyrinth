
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
]

# Define the cities
cities = ['Y', 'E', 'L', 'P', 'M', 'C', 'B', 'I', 'G', 'V', 'J', 'T']

# Find all possible paths that visit E and M exactly twice
all_paths = []
for path in itertools.permutations(cities[1:], 10):
    path = ['Y'] + list(path)
    if path.count('E') == 2 and path.count('M') == 2:
        all_paths.append(path)

# Find the quickest path among all possible paths
quickest_path = None
min_time = float('inf')
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        time += adjacency_matrix[cities.index(path[i])][cities.index(path[i+1])]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
