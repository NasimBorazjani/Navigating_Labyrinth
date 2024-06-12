
import itertools

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
]

# Function to calculate the shortest path using the adjacency matrix
def shortest_path(matrix):
    # Initialize the shortest path
    shortest_path = None
    # Iterate over all permutations of the target cities (P, E)
    for perm in itertools.permutations(['P', 'E']):
        # Calculate the shortest path from Q to the first city, then to the second city, and back to Q
        path = ['Q', perm[0], perm[1], 'Q']
        distance = matrix[0][cities.index(path[1])] + matrix[0][cities.index(path[2])] + matrix[cities.index(path[2])][cities.index(path[3])]
        # Update the shortest path if necessary
        if shortest_path is None or distance < shortest_path[1]:
            shortest_path = (path, distance)
    # Return the shortest path and its distance
    return shortest_path

# List of cities
cities = ['Q', 'O', 'P', 'T', 'W', 'E', 'X', 'M', 'D', 'V']

# Print the shortest path and its distance
print(shortest_path(matrix))
