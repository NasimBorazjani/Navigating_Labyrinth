
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['C', 'Z', 'F', 'U', 'W', 'T', 'H', 'Y', 'P', 'O', 'A', 'R', 'I', 'G', 'B']

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
    if path.count('G') == 2 and path.count('R') == 2 and len(set(path)) == len(path):
        paths.append(path)
    for node in graph[start]:
        if path.count(node) < 2:
            dfs(graph, node, path)

# Find all paths
paths = []
dfs(graph, 'F')

# Print the shortest path
print(min(paths, key=len))
