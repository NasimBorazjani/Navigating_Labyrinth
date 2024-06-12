
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
]

# List of cities
cities = ['S', 'U', 'X', 'D', 'I', 'Z', 'R', 'M', 'K', 'Q']

# Function to calculate the total travel time
def total_travel_time(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += matrix[cities.index(from_city)][cities.index(to_city)]
    return total

# List of cities to visit exactly twice
visit_twice = ['K', 'Q']

# Get all permutations of the cities
perms = list(itertools.permutations(cities))

# Filter out permutations that don't start with 'D'
perms = [perm for perm in perms if perm[0] == 'D']

# Filter out permutations that don't visit 'K' and 'Q' exactly twice
perms = [perm for perm in perms if perm.count('K') == perm.count('Q') == 2]

# Find the permutation with the shortest travel time
shortest_route = min(perms, key=total_travel_time)

print(shortest_route)
