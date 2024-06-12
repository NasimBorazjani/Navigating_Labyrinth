
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
]

# List of cities
cities = ['K', 'M', 'B', 'X', 'N', 'D', 'V', 'C', 'I', 'R', 'F', 'W', 'L']

# Function to calculate total distance
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += matrix[cities.index(from_city)][cities.index(to_city)]
    return total

# Get all permutations of cities excluding B and L twice
perms = list(itertools.permutations(cities[2:]))

# Insert B and L twice into each permutation
routes = [
    ['B', 'L'] + list(perm[i:i+len(cities)-4]) + ['B', 'L']
    for i in range(0, len(perm), len(cities)-4)
    for perm in perms
]

# Find the shortest route
shortest_route = min(routes, key=total_distance)

# Insert C at the beginning
shortest_route.insert(0, 'C')

print(shortest_route)
