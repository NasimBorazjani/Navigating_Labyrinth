
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0]
]

# Define the cities
cities = ['O', 'Z', 'J', 'K', 'E', 'M', 'T', 'W', 'N', 'Q', 'U', 'Y']

# Find all possible paths from O to N to T and back to N and O
all_paths = list(itertools.permutations(['N', 'T'], 2))

# Initialize variables to store the shortest path and its length
shortest_path = []
shortest_length = float('inf')

# Iterate through all possible paths
for path in all_paths:
    current_path = ['O'] + list(path) + ['N', 'O']
    current_length = 0
    
    # Calculate the total length of the current path
    for i in range(len(current_path) - 1):
        current_length += adjacency_matrix[cities.index(current_path[i])][cities.index(current_path[i+1])]
    
    # Update the shortest path if the current path is shorter
    if current_length < shortest_length:
        shortest_path = current_path
        shortest_length = current_length

# Print the shortest path
print(shortest_path)
