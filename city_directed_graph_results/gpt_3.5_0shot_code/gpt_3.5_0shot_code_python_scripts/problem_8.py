
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['Y', 'O', 'Q', 'X', 'K', 'R', 'A', 'U', 'M', 'L']

# Define the starting city
start_city = 'U'

# Find all possible paths that visit A and X exactly twice
all_paths = []
for path in itertools.permutations(cities[1:], 8):
    path = list(path)
    path.insert(0, start_city)
    path.append(start_city)
    if path.count('A') == 2 and path.count('X') == 2:
        all_paths.append(path)

# Calculate the travel time for each path
min_time = float('inf')
quickest_path = []
for path in all_paths:
    time = 0
    for i in range(len(path) - 1):
        time += adjacency_matrix[cities.index(path[i])][cities.index(path[i+1])]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
