
from collections import deque

# Adjacency matrix
matrix = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]
]

# Convert matrix to dictionary
graph = {chr(i + 65): [] for i in range(12)}
for i in range(12):
    for j in range(12):
        if matrix[i][j]:
            graph[chr(i + 65)].append(chr(j + 65))

# BFS
start = 'I'
destinations = ['A', 'X']
path = [start]
visited = {start: 1}
queue = deque([(start, 0)])  # (city, visit count)

while queue:
    city, count = queue.popleft()
    if city in destinations and count == 2:
        continue
    for neighbor in graph[city]:
        if neighbor not in visited or visited[neighbor] < 2:
            queue.append((neighbor, count + 1))
            path.append(neighbor)
            if neighbor not in visited:
                visited[neighbor] = count + 1

# Remove duplicates
path = list(dict.fromkeys(path))

print(path)
