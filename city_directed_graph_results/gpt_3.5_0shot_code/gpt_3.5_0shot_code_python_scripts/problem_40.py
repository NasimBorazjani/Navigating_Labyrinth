
import itertools

# Define the adjacency matrix
adj_matrix = [
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['R', 'L', 'F', 'E', 'D', 'Q', 'G', 'U', 'H', 'T', 'Z', 'A']

# Find all possible paths from city F to city F visiting A and R twice
all_paths = []
for path in itertools.permutations(cities[1:], 10):
    path = ['F'] + list(path) + ['F']
    if path.count('A') == 2 and path.count('R') == 2:
        all_paths.append(path)

# Calculate the total travel time for each path
min_time = float('inf')
quickest_path = None
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        start = cities.index(path[i])
        end = cities.index(path[i+1])
        time += adj_matrix[start][end]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
