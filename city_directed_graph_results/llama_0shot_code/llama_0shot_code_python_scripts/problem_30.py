
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
]

# List of cities
cities = ['S', 'V', 'U', 'W', 'G', 'E', 'H', 'P', 'T', 'Q', 'Z']

# Function to calculate the total travel time
def travel_time(route):
    total = 0
    for i in range(len(route) - 1):
        total += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return total

# Get all possible routes
routes = list(itertools.permutations(cities[1:]))

# Add start and end city to each route
routes = [('G',) + route + ('G',) for route in routes]

# Find the shortest route
shortest_route = min(routes, key=travel_time)

print(shortest_route)
