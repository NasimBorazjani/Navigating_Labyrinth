
from collections import deque

def bfs(graph, start):
    queue = deque([(start, [start])])
    visited = {start: 0}
    while queue:
        node, path = queue.popleft()
        for neighbor, edge in graph[node].items():
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited[neighbor] = len(path)
            elif visited[neighbor] < len(path) - 1 and len(path) > 1:
                queue.append((neighbor, path + [neighbor]))
                visited[neighbor] = len(path)
    return visited

def get_path(visited, start, end):
    return visited[end]

matrix = [
    "001011000000",
    "000101000010",
    "000010010000",
    "001001000100",
    "000100110010",
    "000010010001",
    "001000101000",
    "001000100010",
    "010000100000",
    "001000100010",
    "000010010001",
    "001000100010",
    "000100100010",
    "001000100010"
]

graph = {i: {} for i in range(len(matrix))}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '1':
            graph[i][j] = 1

visited = bfs(graph, 1)

path = get_path(visited, 1, 5)

print(path)
