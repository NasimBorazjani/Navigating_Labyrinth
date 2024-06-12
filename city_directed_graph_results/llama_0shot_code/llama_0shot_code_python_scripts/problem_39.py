
from collections import deque

# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0]
]

# Convert matrix to dictionary
graph = {city: [] for city in 'OZJKEMTWNQUY'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + ord('O'))].append(chr(j + ord('O')))

# BFS
queue = deque([('O', [])])
visited = set()
solution = None

while queue:
    city, path = queue.popleft()
    if city in visited:
        continue
    visited.add(city)
    path = path + [city]
    if city in 'TN' and len(path) == 8:  # We have visited T or N twice
        solution = path
        break
    for neighbor in graph[city]:
        queue.append((neighbor, path))

# Backtrack to find the shortest path
if solution:
    shortest_path = solution
    while len(shortest_path) > 2:
        for city in solution:
            if city in 'TN':
                continue
            path = solution.copy()
            path.remove(city)
            if len(path) == 8:
                shortest_path = path
                break
        else:
            break
        solution = path
    print(shortest_path)
else:
    print('No solution found')
