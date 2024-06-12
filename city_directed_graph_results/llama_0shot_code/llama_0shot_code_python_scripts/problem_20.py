
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
]

# List of cities
cities = ['F', 'I', 'Y', 'R', 'X', 'Q', 'M', 'S', 'C', 'D', 'N']

# Function to calculate the total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# List of cities to visit exactly twice
visit_twice = ['I', 'N']

# Get all permutations of the cities
perms = list(itertools.permutations(cities))

# Filter permutations to include only those that visit I and N twice
valid_perms = [perm for perm in perms if perm.count('I') == perm.count('N') == 2]

# Find the shortest route
shortest_route = min(valid_perms, key=route_distance)

print(shortest_route)
