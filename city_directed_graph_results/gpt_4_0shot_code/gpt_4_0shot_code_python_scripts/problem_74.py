
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
]

# Define the cities
cities = ['O', 'M', 'U', 'L', 'Q', 'P', 'D', 'A', 'S', 'B', 'K', 'V', 'E', 'Z']

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
        if node not in path or node in ['L', 'Z']:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from 'M' to 'L' and 'Z'
paths_to_L = dfs(graph, 'M', 'L')
paths_to_Z = dfs(graph, 'M', 'Z')

# Filter out the paths that visit 'L' and 'Z' exactly twice and other cities at most once
valid_paths = [path for path in paths_to_L + paths_to_Z if path.count('L') == 2 and path.count('Z') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['L', 'Z'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
