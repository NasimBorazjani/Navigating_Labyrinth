
from collections import defaultdict

# The adjacency matrix
matrix = [
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]

# Convert the adjacency matrix into a dictionary
graph = defaultdict(list)
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# DFS function
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            result = dfs(graph, node, end, path)
            if result:
                return result
    return None

# Find the shortest path from 'K' to 'N' and 'K' to 'P'
path_N = dfs(graph, 'K', 'N')
path_P = dfs(graph, 'K', 'P')

# Combine the paths
path = path_N[:-1] + path_P

# Print the solution
print(path)
