
from collections import deque

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]

# Convert matrix to dictionary
graph = {city: [] for city in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# BFS
start = 'L'
targets = ['P', 'W']
path = {city: [] for city in targets}
queue = deque([(start, None)])
visited = set()

while queue:
    city, prev = queue.popleft()
    if city not in visited:
        visited.add(city)
        path[city].append(prev)
        if len(path[city]) == 2:
            break
        for neighbor in graph[city]:
            if neighbor not in visited or (neighbor in targets and len(path[neighbor]) < 2):
                queue.append((neighbor, city))

# Reconstruct the path
final_path = [city for city in path[city] for city in path[neighbor]]
final_path.append(city)
print(final_path)
