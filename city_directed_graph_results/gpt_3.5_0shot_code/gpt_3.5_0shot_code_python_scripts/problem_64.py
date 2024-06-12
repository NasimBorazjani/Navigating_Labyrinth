
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]
]

# Define the cities
cities = ['Z', 'J', 'T', 'D', 'W', 'L', 'P', 'Y', 'V', 'H', 'R', 'I', 'A']

# Define the starting city
start_city = 'Y'

# Find all possible paths from start_city to D and R
possible_paths = []
for path in itertools.permutations(cities, len(cities)):
    if path[0] == start_city and path.count('D') == 2 and path.count('R') == 2:
        possible_paths.append(path)

# Find the quickest path among the possible paths
quickest_path = None
min_time = float('inf')
for path in possible_paths:
    time = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        time += adjacency_matrix[cities.index(current_city)][cities.index(next_city)]
    if time < min_time:
        min_time = time
        quickest_path = path

print(quickest_path)
