
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
]

# Define the cities
cities = ['F', 'O', 'L', 'P', 'Y', 'R', 'Q', 'B', 'T', 'V', 'A', 'K', 'S', 'H']

# Create a dictionary to store the graph
graph = defaultdict(list)

# Populate the graph with the adjacency matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# Define the DFS function
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

# Find all paths from 'T' to 'H' and 'K'
paths_H = dfs(graph, 'T', 'H')
paths_K = dfs(graph, 'T', 'K')

# Filter out the paths that visit 'H' and 'K' exactly twice and other cities at most once
valid_paths = [path for path in paths_H + paths_K if path.count('H') == 2 and path.count('K') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['H', 'K'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)