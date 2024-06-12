
from collections import deque

# Adjacency matrix
matrix = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Convert matrix to dictionary
graph = {city: [] for city in 'V C I Y W Q X K Z T J U F'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# BFS function
def bfs(graph, start, end, visit_twice):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        city, path = queue.popleft()
        if city == end and len(path) == len(visited) + 2:
            return path
        for neighbor in graph[city]:
            if neighbor not in visited and neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
                if neighbor == end:
                    visited.add(neighbor)
        if city not in visited:
            visited.add(city)
    return None

# Find quickest route
route = bfs(graph, 'T', 'V', 2)
if route is None:
    route = bfs(graph, 'T', 'I', 2)
print("[" + ", ".join(route) + "]")
