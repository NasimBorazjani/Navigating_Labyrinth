
from collections import defaultdict

# The adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 0]
]

# Convert the adjacency matrix into a dictionary of lists
graph = defaultdict(list)
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# The DFS function
def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    
    if node == 'A' and path.count('A') < 2:
        return path
    elif node == 'H' and path.count('H') < 2:
        return path
    elif len(path) > 1 and path[-1] in ['A', 'H'] and path.count(path[-1]) == 2:
        return path
    elif len(path) > 1 and path[-1] not in ['A', 'H'] and path[-2] in ['A', 'H']:
        return path
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            result = dfs(graph, neighbour, visited, path)
            if result:
                return result
    
    path.pop()
    visited.remove(node)

# Find the quickest route
route = dfs(graph, 'W', set(), [])
print(route)
