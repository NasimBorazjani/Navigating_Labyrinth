
from collections import deque

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

# Convert matrix to dictionary
graph = {chr(i+65): [] for i in range(13)}
for i in range(13):
    for j in range(13):
        if matrix[i][j]:
            graph[chr(i+65)].append(chr(j+65))

# BFS
def bfs(graph, start, end1, end2):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        path = queue.popleft()
        city = path[-1]
        if (city == end1 and end1 in path[1:] and end2 in path[1:]) or (city == end2 and end2 in path[1:] and end1 in path[1:]):
            return path
        for next_city in graph[city]:
            if next_city not in visited:
                visited.add(next_city)
                queue.append(path + [next_city])
    return None

# Find shortest path
path = bfs(graph, 'K', 'U', 'Y')
print(path)
