
from collections import defaultdict

# Create a graph from the adjacency matrix
graph = {
    'D': ['T', 'E', 'J', 'Q'],
    'T': ['L', 'E', 'Q', 'O'],
    'L': ['E'],
    'E': ['J', 'Q', 'O', 'K'],
    'C': ['D'],
    'J': ['F'],
    'Q': ['L', 'O', 'F'],
    'O': ['D', 'J', 'K', 'X'],
    'K': ['T', 'L', 'C', 'X'],
    'X': ['D'],
    'F': ['D', 'T', 'L', 'C', 'J']
}

# Perform a DFS to find all possible paths
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == 8 and path.count('D') == 2 and path.count('E') == 2:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or (node in ['D', 'E'] and path.count(node) < 2):
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find the quickest route
paths = dfs(graph, 'J')
quickest_route = min(paths, key=len)
print(quickest_route)
