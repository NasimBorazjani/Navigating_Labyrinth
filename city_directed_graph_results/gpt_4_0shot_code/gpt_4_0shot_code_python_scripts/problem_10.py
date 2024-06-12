
from collections import defaultdict

# Create a graph from the adjacency matrix
graph = {
    'Q': ['M'],
    'O': ['E'],
    'P': ['T', 'W', 'M', 'D', 'V'],
    'T': ['W', 'M'],
    'W': ['O', 'E', 'V'],
    'E': ['X'],
    'X': ['P', 'V'],
    'M': ['O', 'X', 'V'],
    'D': ['O', 'T', 'X', 'M', 'V'],
    'V': ['Q', 'O', 'P', 'E']
}

# Function to perform DFS
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == 10 and path.count('P') == 2 and path.count('E') == 2:
        return path
    for node in graph[start]:
        if path.count(node) < 2:
            newpath = dfs(graph, node, path)
            if newpath:
                return newpath
    return None

# Find the quickest route
route = dfs(graph, 'Q')
print(route)
