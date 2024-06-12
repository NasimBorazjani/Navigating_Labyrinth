
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

# Define the cities
cities = ['O', 'T', 'F', 'C', 'K', 'U', 'X', 'G', 'A', 'M', 'W', 'Y']

# Find all possible paths that visit K and M exactly twice
all_paths = []
for path in itertools.permutations(cities[1:], len(cities)-1):
    if path.count('K') == 2 and path.count('M') == 2:
        all_paths.append(path)

# Find the quickest path among all possible paths
quickest_path = None
min_time = float('inf')
for path in all_paths:
    time = 0
    current_city = 'O'
    for city in path:
        time += adjacency_matrix[cities.index(current_city)][cities.index(city)]
        current_city = city
    if time < min_time:
        min_time = time
        quickest_path = ['O'] + list(path)

print(quickest_path)
