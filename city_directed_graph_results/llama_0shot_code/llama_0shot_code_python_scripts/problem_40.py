
import itertools

# Adjacency matrix
matrix = [
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

# List of cities
cities = ['R', 'L', 'F', 'E', 'D', 'Q', 'G', 'U', 'H', 'T', 'Z', 'A']

# Function to calculate the total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# Get all possible routes (permutations) of length 12 (2 visits to R and A, and 8 stops)
routes = list(itertools.permutations(cities * 2))

# Find the shortest route
shortest_route = min(routes, key=route_distance)

# Print the solution
print(shortest_route)
