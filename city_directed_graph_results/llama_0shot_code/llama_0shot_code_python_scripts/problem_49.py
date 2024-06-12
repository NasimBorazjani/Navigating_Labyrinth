
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
]

# List of cities
cities = ['W', 'D', 'R', 'A', 'Y', 'F', 'C', 'S', 'N', 'E', 'K', 'Q']

# Function to calculate total travel time
def travel_time(path):
    total = 0
    for i in range(len(path) - 1):
        total += matrix[cities.index(path[i])][cities.index(path[i + 1])]
    return total

# Get all permutations of cities
perms = list(itertools.permutations(cities[1:]))

# Insert 'E' at the start and 'E' at the end of each permutation
perms = [('E',) + p + ('E',) for p in perms]

# Find the shortest path
shortest_path = min(perms, key=travel_time)

# Print the shortest path
print(shortest_path)
