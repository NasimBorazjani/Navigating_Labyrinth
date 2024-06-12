
from collections import deque

# adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
]

# convert matrix to dictionary
graph = {chr(i+65): [] for i in range(13)}
for i in range(13):
    for j in range(13):
        if matrix[i][j]:
            graph[chr(i+65)].append(chr(j+65))

# BFS
start = 'U'
targets = ['H', 'L']
path = [start]
visited = {node: 0 for node in graph}
queue = deque([(start, 0)])

while queue:
    node, count = queue.popleft()
    if node in targets and visited[node] < 2:
        path.append(node)
        visited[node] += 1
        if visited[node] < 2:
            queue.append((node, count+1))
    else:
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                queue.append((neighbor, count+1))
                visited[neighbor] += 1

print(path)
