
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
]

# List of cities
cities = ['I', 'K', 'D', 'M', 'Y', 'H', 'C', 'R', 'V', 'W', 'Q']

# Function to calculate total distance
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += matrix[cities.index(from_city)][cities.index(to_city)]
    return total

# Initialize minimum distance to a large number
min_distance = float('inf')

# Iterate over all permutations of cities
for route in itertools.permutations(cities[1:]):
    # Add start city to the route
    route = ['Y'] + list(route)
    # Calculate total distance
    distance = total_distance(route)
    # Update minimum distance if necessary
    if distance < min_distance:
        min_distance = distance
        min_route = route

# Print the route with minimum distance
print(min_route)
