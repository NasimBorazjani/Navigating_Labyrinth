
from collections import defaultdict

# Define the adjacency matrix
matrix = {
    'Z': ['P', 'B', 'Y', 'C'],
    'H': ['Z', 'P', 'L', 'Q', 'Y', 'V', 'C'],
    'M': ['H', 'Y', 'V'],
    'P': ['B', 'E', 'C'],
    'B': ['H', 'I'],
    'I': ['H', 'B', 'E', 'Q', 'C'],
    'E': ['Z', 'H', 'M'],
    'L': ['Z', 'H', 'M', 'B', 'I', 'E', 'Q'],
    'Q': ['Z', 'M', 'P', 'B', 'E', 'L'],
    'Y': ['L', 'V', 'C'],
    'V': ['M'],
    'C': ['B', 'Y']
}

# Define the DFS function
def dfs(city, path, visited):
    visited.add(city)
    path.append(city)
    if len(path) > 2 and path.count('M') == 2 and path.count('Q') == 2:
        paths.append(path.copy())
    for next_city in matrix[city]:
        if next_city not in visited or next_city in ['M', 'Q']:
            dfs(next_city, path, visited)
    path.pop()
    visited.remove(city)

# Find all possible paths
paths = []
dfs('C', [], set())

# Filter out the paths that visit 'M' and 'Q' exactly twice and other cities at most once
valid_paths = [path for path in paths if all(path.count(city) == 1 for city in set(path) - {'M', 'Q'})]

# Return the shortest path
print(min(valid_paths, key=len))
