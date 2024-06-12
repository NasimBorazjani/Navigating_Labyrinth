
from collections import deque

# Adjacency matrix
matrix = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

# Convert matrix to dictionary
graph = {i: [] for i in range(len(matrix))}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[i].append(j)

# BFS
start = 1  # City 'B'
targets = [8, 9]  # Cities 'Q' and 'I'
visited = {node: 0 for node in graph}
visited[start] = 1
queue = deque([(start, [start])])

while queue:
    node, path = queue.popleft()
    for neighbor in graph[node]:
        if neighbor in targets and visited[neighbor] < 2:
            visited[neighbor] += 1
            if visited[neighbor] == 2:
                # We have visited both targets exactly twice
                path.append(neighbor)
                print(path)
                exit()
        elif visited[neighbor] == 0:
            visited[neighbor] = 1
            queue.append((neighbor, path + [neighbor]))
