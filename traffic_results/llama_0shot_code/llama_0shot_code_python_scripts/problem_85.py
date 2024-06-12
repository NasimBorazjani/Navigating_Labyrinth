
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def neighbors(i, j):
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                yield ni, nj

    def heuristic(i, j):
        return abs(i - 10) + abs(j - 12) + abs(i - 4) + abs(j - 3)

    start, end = (10, 12), (4, 3)
    queue = [(heuristic(*start), (*start, []))]
    visited = set()

    while queue:
        _, (i, j, path) = heapq.heappop(queue)
        if (i, j) not in visited:
            visited.add((i, j))
            path = [(*start, *end)]
            if (i, j) == end:
                return path
            for ni, nj in neighbors(i, j):
                heapq.heappush(queue, (heuristic(ni, nj), (*end, [*path, (ni, nj)])))

    return None

matrix = [
    [5, 10, 'x', 'x', 'x', 16, 'x', 'x', 16, 'x', 10, 8, 'x'],
    [1, 'x', 13, 'x', 7, 'x', 'x', 'x', 10, 3, 3, 13, 18, 11],
    # ...
]

print(shortest_path(matrix))
