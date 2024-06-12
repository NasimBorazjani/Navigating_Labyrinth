
from collections import defaultdict

# Define the adjacency matrix
adjacency_matrix = {
    'G': ['H'],
    'D': ['P'],
    'X': ['G', 'Y', 'W'],
    'N': ['W', 'A', 'H'],
    'Y': ['X', 'N', 'A'],
    'W': ['X'],
    'A': ['G', 'D', 'X', 'H', 'V'],
    'P': ['G', 'Y', 'H'],
    'V': ['G', 'P'],
    'H': ['G', 'D', 'N', 'A', 'P']
}

# Define the function to find the path
def find_path(city, visited, path):
    visited[city] = True
    path.append(city)

    if len(path) == 2 and path.count('A') == 2 and path.count('H') == 2:
        print(path)
    else:
        for neighbor in adjacency_matrix[city]:
            if visited[neighbor] == False or (neighbor in ['A', 'H'] and path.count(neighbor) < 2):
                find_path(neighbor, visited, path)

    path.pop()
    visited[city] = False

# Initialize visited dictionary and path list
visited = defaultdict(bool)
path = []

# Call the function
find_path('W', visited, path)
