
from collections import defaultdict

# Create a graph from the adjacency matrix
graph = {
    'U': ['K', 'T'],
    'W': ['U', 'J'],
    'A': ['X', 'R'],
    'J': ['U', 'A', 'E'],
    'K': ['W', 'J', 'T'],
    'H': ['W', 'E'],
    'E': ['R'],
    'X': ['W', 'H'],
    'R': ['U', 'K', 'H', 'E', 'T'],
    'T': ['U', 'W', 'A', 'H', 'X']
}

# Perform a DFS to find all possible paths
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from 'E' to 'W' and 'X'
paths_to_w = dfs(graph, 'E', 'W')
paths_to_x = dfs(graph, 'E', 'X')

# Check if each path visits 'W' and 'X' exactly twice and doesn't visit any other city more than once
valid_paths = []
for path in paths_to_w + paths_to_x:
    if path.count('W') == 2 and path.count('X') == 2 and all(path.count(city) <= 1 for city in set(path) - {'W', 'X'}):
        valid_paths.append(path)

# Return the shortest valid path
print(min(valid_paths, key=len))
