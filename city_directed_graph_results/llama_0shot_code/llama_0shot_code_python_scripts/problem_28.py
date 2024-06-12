
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
]

# List of cities
cities = ['A', 'N', 'B', 'M', 'Z', 'O', 'E', 'Q', 'G', 'L', 'P']

# Function to calculate the total travel time
def travel_time(route):
    total = 0
    for i in range(len(route) - 1):
        total += matrix[cities.index(route[i])][cities.index(route[i + 1])]
    return total

# List of cities to visit (excluding the start city)
to_visit = ['E', 'N']

# Generate all possible routes
routes = list(itertools.permutations(cities[1:]))

# Find the shortest route
shortest_route = None
shortest_time = float('inf')

for route in routes:
    # Insert the start city at the beginning of each route
    route = ['B'] + list(route)
    # Check if the route visits all the required cities exactly twice
    counts = {city: route.count(city) for city in to_visit}
    if all(count == 2 for count in counts.values()):
        # Calculate the total travel time
        time = travel_time(route)
        # Update the shortest route and time
        if time < shortest_time:
            shortest_route = route
            shortest_time = time

print(shortest_route)
