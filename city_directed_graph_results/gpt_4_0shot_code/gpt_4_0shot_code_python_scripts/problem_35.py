
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['A', 'V', 'N', 'Q', 'P', 'S', 'M', 'E', 'L', 'H', 'W', 'G']

# Create a dictionary to store the graph
graph = defaultdict(list)

# Convert the adjacency matrix to a graph
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
        if node not in path or (node == 'L' and path.count('L') < 2) or (node == 'P' and path.count('P') < 2):
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from 'G' to 'L' and 'P'
paths = dfs(graph, 'G', 'L') + dfs(graph, 'G', 'P')

# Filter out the paths that visit 'L' and 'P' exactly twice and other cities at most once
valid_paths = [path for path in paths if path.count('L') == 2 and path.count('P') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['L', 'P'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
