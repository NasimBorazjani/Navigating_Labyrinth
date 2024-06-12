
from collections import deque

def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        workshop = path[-1]
        if workshop == end:
            return path
        for neighbor, time in graph[workshop]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def solve(matrix, start, end):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 'x':
                graph[(i, j)] = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 'x':
                        graph[(i, j)].append(((x, y), matrix[i][j]))
    return bfs(graph, start, end)

matrix = [
    ['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14],
    ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 'x'],
    [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15],
    ['x', 4, 'x', 'x', 18, 9, 'x', 15, 'x', 1, 9],
    [3, 2, 7, 'x', 'x', 17, 2, 14, 'x', 4, 2],
    [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7],
    ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4],
    ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'],
    ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'],
    ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'],
    ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]
]
start = (3, 10)
end = (6, 2)
print(solve(matrix, start, end))
