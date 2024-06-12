
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['A', 'V', 'N', 'Q', 'P', 'S', 'M', 'E', 'L', 'H', 'W', 'G']

# Define the starting city
start_city = 'G'

# Find all possible paths from G to L and P exactly twice
all_paths = []
for path in itertools.permutations(['L', 'P', 'L', 'P']):
    all_paths.append([start_city] + list(path))

# Find the shortest path among all possible paths
shortest_path = None
min_distance = float('inf')

for path in all_paths:
    distance = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        distance += adjacency_matrix[cities.index(current_city)][cities.index(next_city)]
    
    if distance < min_distance:
        min_distance = distance
        shortest_path = path

print(shortest_path)
