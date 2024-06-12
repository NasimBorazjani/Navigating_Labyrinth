
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['D', 'T', 'L', 'E', 'C', 'J', 'Q', 'O', 'K', 'X', 'F']

# Define the starting city
start_city = 'J'

# Find all possible paths that visit D and E twice
all_paths = []
for path in itertools.permutations(cities[1:], 9):
    path = [start_city] + list(path) + [start_city]
    if path.count('D') == 2 and path.count('E') == 2:
        all_paths.append(path)

# Calculate the travel time for each path
min_time = float('inf')
min_path = None
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        from_city = cities.index(path[i])
        to_city = cities.index(path[i + 1])
        time += adjacency_matrix[from_city][to_city]
    if time < min_time:
        min_time = time
        min_path = path

print(min_path)
