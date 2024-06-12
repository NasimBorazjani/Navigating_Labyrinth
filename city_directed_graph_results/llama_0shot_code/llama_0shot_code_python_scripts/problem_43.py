
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
]

# List of cities
cities = ['Y', 'E', 'L', 'P', 'M', 'C', 'B', 'I', 'G', 'V', 'J', 'T']

# Function to calculate total travel time
def total_travel_time(path):
    total = 0
    for i in range(len(path) - 1):
        city1 = path[i]
        city2 = path[i + 1]
        total += matrix[cities.index(city1)][cities.index(city2)]
    return total

# Check all possible paths
min_travel_time = float('inf')
min_path = None
for path in itertools.permutations(cities[1:]):
    path = ['Y'] + list(path) + ['Y']
    travel_time = total_travel_time(path)
    if travel_time < min_travel_time:
        min_travel_time = travel_time
        min_path = path

print(min_path)
