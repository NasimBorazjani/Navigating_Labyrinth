
from collections import deque

# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
]

# Convert matrix to dictionary
graph = {city: [] for city in 'IPGSAYDUEVWHZX'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# BFS
start = 'Y'
destinations = ['H', 'X']
path = [start]
visited = set(path)
queue = deque(path)

while queue:
    city = queue.popleft()
    for neighbor in graph[city]:
        if neighbor in destinations and neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)
            queue.append(neighbor)
        elif neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)
            queue.append(neighbor)

        if set(destinations).issubset(visited):
            return path

if set(destinations).issubset(visited):
    return path
else:
    return "No solution found"
