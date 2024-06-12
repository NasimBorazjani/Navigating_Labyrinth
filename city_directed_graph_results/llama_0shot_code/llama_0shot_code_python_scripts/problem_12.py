
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

# List of cities
cities = ['S', 'T', 'R', 'A', 'L', 'B', 'V', 'I', 'P', 'N']

# Function to calculate total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# Get all possible routes that visit each city once and return to the starting city
routes = [route for route in itertools.permutations(cities[1:]) if route[0] in ['L', 'V'] and route[-1] in ['L', 'V']]

# Find the shortest route
shortest_route = min(routes, key=route_distance)

# Add the start city and the two destination cities to the route
shortest_route = ['B'] + list(shortest_route) + ['B']

print(shortest_route)
