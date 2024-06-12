
from collections import defaultdict

# adjacency matrix
matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
]

# city names
cities = ['K', 'M', 'B', 'X', 'N', 'D', 'V', 'C', 'I', 'R', 'F', 'W', 'L']

# create graph from adjacency matrix
graph = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[cities[i]].append(cities[j])

# DFS algorithm
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(cities):
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or (node in ['B', 'L'] and path.count(node) < 2):
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# find all paths
paths = dfs(graph, 'C')

# filter out the paths that visit city 'B' and city 'L' exactly twice
paths = [path for path in paths if path.count('B') == 2 and path.count('L') == 2]

# find the shortest path
shortest_path = min(paths, key=len)

print(shortest_path)
