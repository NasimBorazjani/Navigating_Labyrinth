
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]
]

# All possible routes
routes = list(itertools.permutations(['P', 'U', 'Q', 'G', 'E', 'K', 'M', 'J', 'N', 'T', 'Y', 'R', 'Z', 'X', 'O']))

# Function to calculate the total distance of a route
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total_distance += matrix[cities.index(from_city)][cities.index(to_city)]
    return total_distance

# List of cities
cities = ['P', 'U', 'Q', 'G', 'E', 'K', 'M', 'J', 'N', 'T', 'Y', 'R', 'Z', 'X', 'O']

# Find the shortest route
shortest_route = min(routes, key=calculate_distance)

print(shortest_route)
