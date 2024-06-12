
import itertools

# Define the adjacency matrix
adj_matrix = [
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
]

# Define the cities
cities = ['F', 'O', 'L', 'P', 'Y', 'R', 'Q', 'B', 'T', 'V', 'A', 'K', 'S', 'H']

# Define the starting city
start_city = 'T'

# Find all possible paths from T to H and K
all_paths = []
for perm in itertools.permutations([11, 13]):
    path = [start_city]
    for p in perm:
        path.append(cities[p])
    all_paths.append(path)

# Find the shortest path
shortest_path = None
min_time = float('inf')
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        time += adj_matrix[cities.index(path[i])][cities.index(path[i+1])]
    if time < min_time:
        min_time = time
        shortest_path = path

print(shortest_path)
