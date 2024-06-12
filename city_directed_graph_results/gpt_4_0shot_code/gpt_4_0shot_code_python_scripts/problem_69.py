
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0]
]
cities = ['N', 'Y', 'P', 'L', 'Q', 'H', 'C', 'G', 'U', 'K', 'J', 'B', 'R', 'T']

# Create a graph from the adjacency matrix
graph = defaultdict(list)
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

# Find all paths from 'P' to 'N' and 'R'
paths_to_n = dfs(graph, 'P', 'N')
paths_to_r = dfs(graph, 'P', 'R')

# Filter out the paths that visit 'N' and 'R' exactly twice and other cities at most once
valid_paths = []
for path_to_n in paths_to_n:
    for path_to_r in paths_to_r:
        path = path_to_n + path_to_r[1:]
        if path.count('N') == 2 and path.count('R') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['N', 'R']):
            valid_paths.append(path)

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
