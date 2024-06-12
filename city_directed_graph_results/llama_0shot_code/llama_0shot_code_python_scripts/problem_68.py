
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
]

# List of cities
cities = ['P', 'G', 'W', 'V', 'L', 'M', 'B', 'S', 'J', 'H', 'D', 'N', 'R']

# Function to calculate the total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# List to store the best route found so far
best_route = None

# Iterate over all permutations of the cities (excluding the start city)
for route in itertools.permutations(cities[1:]):
    # Add the start city to the route
    route = ['P'] + list(route)
    # Calculate the total distance of the route
    distance = route_distance(route)
    # Check if this route is the best found so far
    if best_route is None or distance < route_distance(best_route):
        best_route = route

print(best_route)
