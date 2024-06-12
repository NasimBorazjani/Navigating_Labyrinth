
from collections import defaultdict

# Create a graph from the adjacency matrix
graph = {
    'Y': ['J'],
    'E': ['P', 'B'],
    'L': ['E', 'M', 'C', 'T'],
    'P': ['L'],
    'M': ['P', 'T'],
    'C': ['P', 'M', 'B'],
    'B': ['E', 'P', 'V', 'J'],
    'I': ['Y', 'E', 'M', 'B', 'G'],
    'G': ['Y', 'E'],
    'V': ['M'],
    'J': ['P', 'B', 'I', 'G', 'T'],
    'T': ['C', 'I', 'G']
}

# Function to perform DFS
def dfs(graph, start, path=[]):
    path = path + [start]
    if path.count('E') == 2 and path.count('M') == 2 and len(set(path)) == len(path):
        return path
    for node in graph[start]:
        if path.count(node) < 2:
            newpath = dfs(graph, node, path)
            if newpath:
                return newpath
    return []

# Find the quickest route
route = dfs(graph, 'Y')
print(route)
