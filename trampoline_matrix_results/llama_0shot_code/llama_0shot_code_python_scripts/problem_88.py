
from collections import deque

def create_graph(grid):
    n = len(grid)
    graph = {(i, j): [] for i in range(n) for j in range(n)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    graph[(i, j)].append((ni, nj))
    return graph

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

grid = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
]

graph = create_graph(grid)
start, end = (0, 11), (9, 1)
path = bfs(graph, start, end)
print(path)
