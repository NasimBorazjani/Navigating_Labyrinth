
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
]

# Define the cities
cities = ['S', 'X', 'G', 'E', 'P', 'B', 'O', 'C', 'L', 'J', 'M', 'Y', 'T', 'W']

# Create a graph from the adjacency matrix
graph = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# Define the DFS function
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(cities):
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or (node in ['M', 'B'] and path.count(node) < 2):
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from 'Y'
all_paths = dfs(graph, 'Y')

# Filter out the paths that visit 'M' and 'B' exactly twice and other cities at most once
valid_paths = [path for path in all_paths if path.count('M') == 2 and path.count('B') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['M', 'B'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
