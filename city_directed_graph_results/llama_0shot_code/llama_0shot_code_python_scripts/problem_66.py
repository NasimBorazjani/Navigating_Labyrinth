
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]
]

# Convert the adjacency matrix into a dictionary
graph = {city1: {city2: time for city2, time in enumerate(row) if time == 1} for city1, row in enumerate(matrix)}

# Function to calculate the total travel time of a route
def total_travel_time(route):
    return sum(graph[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Generate all possible routes from city 'L' visiting J and K exactly twice
routes = [route for route in itertools.permutations(["L", "A", "J", "U", "E", "P", "Q", "Y", "H", "R", "K", "M", "F"]) if route.count("J") == route.count("K") == 2]

# Select the route with the shortest total travel time
shortest_route = min(routes, key=total_travel_time)

print(shortest_route)
