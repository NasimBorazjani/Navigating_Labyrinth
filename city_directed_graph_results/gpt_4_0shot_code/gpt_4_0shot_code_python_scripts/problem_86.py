
from collections import defaultdict

# adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0]
]

# city names
cities = ['P', 'U', 'Q', 'G', 'E', 'K', 'M', 'J', 'N', 'T', 'Y', 'R', 'Z', 'X', 'O']

# create a graph from the adjacency matrix
graph = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# DFS algorithm
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(cities) and path.count('P') == 2 and path.count('Y') == 2:
        paths.append(path)
    for node in graph[start]:
        if path.count(node) < 2 or (node in ['P', 'Y'] and path.count(node) < 3):
            dfs(graph, node, path)

# find all paths
paths = []
dfs(graph, 'G')

# find the shortest path
shortest_path = min(paths, key=len)

print(shortest_path)
