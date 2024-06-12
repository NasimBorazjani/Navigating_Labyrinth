
from collections import deque

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
]

# Convert matrix to dictionary
graph = {city: [] for city in 'ZJTDWLPRYVHRAI'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# BFS
start = 'Y'
destinations = {'D', 'R'}
path = [start]
visited = {start: 0}
queue = deque([start])

while queue:
    city = queue.popleft()
    for neighbor in graph[city]:
        if neighbor in destinations:
            if visited.get(neighbor, 0) < 2:
                queue.append(neighbor)
                visited[neighbor] = visited.get(neighbor, 0) + 1
        elif neighbor not in visited:
            queue.append(neighbor)
            visited[neighbor] = 1
            path.append(neighbor)

# Ensure we have visited D and R exactly twice
assert all(visited[city] == 2 for city in destinations)

print(path)
