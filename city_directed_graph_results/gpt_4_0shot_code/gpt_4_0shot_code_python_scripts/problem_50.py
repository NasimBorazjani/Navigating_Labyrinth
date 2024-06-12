
from collections import defaultdict

# Define the adjacency matrix
matrix = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]
]

# Define the cities
cities = ['I', 'E', 'A', 'G', 'V', 'K', 'B', 'N', 'F', 'W', 'J', 'O']

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
        if node not in path:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find all paths from 'E' to 'N' and 'O'
paths_to_n = dfs(graph, 'E', 'N')
paths_to_o = dfs(graph, 'E', 'O')

# Filter out the paths that visit 'N' and 'O' exactly twice and other cities at most once
valid_paths = [path for path in paths_to_n + paths_to_o if path.count('N') == 2 and path.count('O') == 2 and all(path.count(city) <= 1 for city in cities if city not in ['N', 'O'])]

# Find the shortest path
shortest_path = min(valid_paths, key=len)

print(shortest_path)
