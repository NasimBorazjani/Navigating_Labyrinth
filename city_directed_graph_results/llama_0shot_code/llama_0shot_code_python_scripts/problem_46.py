
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

# List of cities
cities = ['O', 'T', 'F', 'C', 'K', 'U', 'X', 'G', 'A', 'M', 'W', 'Y']

# Function to calculate the total distance of a path
def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += matrix[cities.index(path[i])][cities.index(path[i + 1])]
    return total

# Function to find the shortest path
def shortest_path():
    # Get all possible paths
    paths = list(itertools.permutations(cities[1:]))
    # Add 'O' at the start and end of each path
    paths = ['O'] + list(paths) + ['O']
    # Find the shortest path
    shortest_path = min(paths, key=total_distance)
    return shortest_path

# Print the shortest path
print(shortest_path())
