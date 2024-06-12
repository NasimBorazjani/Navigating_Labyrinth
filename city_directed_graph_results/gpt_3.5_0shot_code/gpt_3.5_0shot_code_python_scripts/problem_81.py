
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
]

# Define the cities
cities = ['T', 'J', 'X', 'U', 'L', 'S', 'C', 'H', 'Z', 'O', 'D', 'Q', 'G', 'W']

# Find all possible paths from U to H to L and back to H
all_paths = list(itertools.permutations(['H', 'L'], 2))

# Initialize variables to store the shortest path and its length
shortest_path = []
shortest_path_length = float('inf')

# Iterate through all possible paths
for path in all_paths:
    current_path = ['U'] + list(path) + list(path) + ['U']
    current_path_length = 0
    
    # Calculate the length of the current path
    for i in range(len(current_path) - 1):
        start_city = cities.index(current_path[i])
        end_city = cities.index(current_path[i + 1])
        current_path_length += adjacency_matrix[start_city][end_city]
    
    # Update the shortest path if the current path is shorter
    if current_path_length < shortest_path_length:
        shortest_path = current_path
        shortest_path_length = current_path_length

# Print the shortest path
print(shortest_path)
