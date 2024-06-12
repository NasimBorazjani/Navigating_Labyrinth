
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
]

# List of cities
cities = ['G', 'X', 'R', 'L', 'Y', 'E', 'V', 'T', 'B', 'H']

# Function to calculate the total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# List of routes that visit cities E and X exactly twice
routes = [route for route in itertools.permutations(cities) if route.count('E') == 2 and route.count('X') == 2]

# Find the shortest route
shortest_route = min(routes, key=route_distance)

print(shortest_route)
