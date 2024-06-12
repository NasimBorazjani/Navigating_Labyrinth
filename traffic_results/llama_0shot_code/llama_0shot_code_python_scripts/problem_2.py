
import heapq

def dijkstra(matrix, start, end):
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    prev = [[None for _ in range(n)] for _ in range(m)]
    heap = [(matrix[start[0]][start[1]], start)]
    while heap:
        d, (i, j) = heapq.heappop(heap)
        if (i, j) == end:
            path = []
            while (i, j) is not None:
                path.append((i, j))
                i, j = prev[i][j]
            return path[::-1]
        if visited[i][j]:
            continue
        visited[i][j] = 1
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != 'x':
                heapq.heappush(heap, (matrix[ni][nj], (ni, nj)))
                prev[ni][nj] = (i, j)
    return []

def get_path(matrix, start, end):
    matrix = [[int(x) if x != 'x' else float('inf') for x in row] for row in matrix]
    return dijkstra(matrix, start, end)

matrix = [
    ['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
    ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
    [8, 'x', 2, 5, 6, 12, 9, 10, 7],
    [12, 1, 6, 20, 19, 18, 12, 'x', 14],
    [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
    ['x', 3, 'x', 'x', 'x', 'x', 'x', 4],
    [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
    ['x', 5, 'x', 'x', 'x', 17, 9, 'x'],
    [13, 16, 8, 15, 'x', 2, 'x', 1, 2]
]

start = (2, 2)
end = (5, 8)

print(get_path(matrix, start, end))
