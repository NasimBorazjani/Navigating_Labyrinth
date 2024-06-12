
from collections import defaultdict

# Create a graph from the adjacency matrix
graph = {
    'F': ['J', 'K', 'M'],
    'I': ['F', 'B'],
    'O': ['J', 'D', 'M', 'B'],
    'J': ['F', 'O'],
    'K': ['O', 'D'],
    'D': ['I', 'O', 'R'],
    'N': ['I', 'R'],
    'R': ['J', 'M'],
    'M': ['F', 'I', 'J'],
    'B': ['F', 'O', 'M']
}

# Perform a DFS to find all possible paths
def dfs(graph, start, path=[]):
    path = path + [start]
    if len(path) == 10:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or (node in ['D', 'F'] and path.count(node) < 2):
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Find the shortest path that visits 'D' and 'F' exactly twice
def find_path(graph, start):
    paths = dfs(graph, start)
    paths = [path for path in paths if path.count('D') == 2 and path.count('F') == 2]
    if not paths:
        return None
    shortest = min(paths, key=len)
    return shortest

print(find_path(graph, 'N'))
