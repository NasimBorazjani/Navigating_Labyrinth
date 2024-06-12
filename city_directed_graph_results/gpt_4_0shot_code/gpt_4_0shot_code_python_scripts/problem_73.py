
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['K', 'N', 'S', 'Y', 'O', 'I', 'T', 'D', 'M', 'Z', 'R', 'B', 'E', 'F']

# Create a dictionary to store the graph
graph = defaultdict(list)

# Convert the adjacency matrix to a graph
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# Define the DFS function
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(cities):
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(dfs(graph, node, path))
    return paths

# Get all possible paths
paths = dfs(graph, 'Y')

# Filter out the paths that visit city 'S' and city 'K' exactly twice and other cities at most once
valid_paths = [path for path in paths if path.count('S') == 2 and path.count('K') == 2 and all(path.count(city) <= 1 for city in cities if city != 'S' and city != 'K')]

# Get the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
