
from collections import defaultdict

# Define the adjacency matrix
matrix = [
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

# Create a dictionary to store the graph
graph = defaultdict(list)

# Populate the graph with the adjacency matrix
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
        if node not in path:
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all possible paths
all_paths = dfs(graph, 'U')

# Filter out the paths that visit city 'H' and 'L' exactly twice and other cities at most once
valid_paths = [path for path in all_paths if path.count('H') == 2 and path.count('L') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['H', 'L'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
