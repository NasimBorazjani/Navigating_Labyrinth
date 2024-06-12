
# Adjacency matrix
matrix = [
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]

# Convert the adjacency matrix to a dictionary of lists
graph = {city: [] for city in 'RBZNHAPMJ'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath:
                return newpath
    return None

# Find the shortest path from 'Z' to 'B' and 'H'
path_B = dfs(graph, 'Z', 'B')
path_H = dfs(graph, 'Z', 'H')

# Combine the paths and remove the redundant parts
path = path_B[:path_B.index('B')+1] + path_H[path_H.index('H')+1:]

# Add the start city 'Z' to the beginning of the path
path.insert(0, 'Z')

print(path)
