
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0]
]

# List of cities
cities = ['L', 'Y', 'V', 'E', 'A', 'M', 'C', 'Q', 'F', 'Z', 'G', 'O']

# Function to calculate the total distance of a route
def route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return distance

# Get all possible routes (permutations) of length 12 (2 visits to each city + 2 visits to A and Y + 1 visit to E)
routes = list(itertools.permutations(cities * 2 + ['E']))

# Find the shortest route
shortest_route = min(routes, key=route_distance)

# Print the solution
print(shortest_route)
