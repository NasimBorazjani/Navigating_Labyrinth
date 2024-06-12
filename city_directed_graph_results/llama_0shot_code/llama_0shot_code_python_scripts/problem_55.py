
from collections import deque

# Adjacency matrix
matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
]

# Convert matrix to dictionary
graph = {chr(65 + i): [] for i in range(13)}
for i in range(13):
    for j in range(13):
        if matrix[i][j]:
            graph[chr(65 + i)].append(chr(65 + j))

# BFS
start = 'H'
destinations = ['B', 'X']
path = [start]
visited = {node: 0 for node in graph}
queue = deque([(start, 0)])

while queue:
    node, count = queue.popleft()
    if node in destinations:
        visited[node] += 1
        if visited[node] == 2:
            path.append(node)
            if len(path) == 14:  # 13 nodes + start
                break
            continue
    for neighbor in graph[node]:
        if visited[neighbor] < 2:
            queue.append((neighbor, count + 1))
            visited[neighbor] += 1

if len(path) != 14:
    print("No solution")
else:
    print(path)
