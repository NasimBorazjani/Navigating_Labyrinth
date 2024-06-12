
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    while queue:
        time, (r, c) = heapq.heappop(queue)
        if (r, c) not in visited:
            visited.add((r, c))
            if (r, c) == end:
                path = [end]
                while (r, c) != start:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(rows) and nc in range(cols) and matrix[nr][nc] != 'x':
                            if (nr, nc) in visited:
                                r, c = nr, nc
                                path.append((nr, nc))
                                break
                return path[::-1]
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) not in visited:
                    heapq.heappush(queue, (time + matrix[nr][nc], (nr, nc)))
    return []

matrix = [
    ['x', 'x', 'x', 'x', 13, 'x', 'x', 3, 8],
    ['x', 18, 19, 19, 2, 9, 'x', 'x', 'x'],
    [15, 'x', 6, 'x', 'x', 'x', 13, 13, 4],
    [7, 'x', 4, 10, 'x', 11, 10, 17, 'x'],
    [2, 7, 'x', 'x', 8, 16, 4, 1, 4],
    ['x', 'x', 'x', 5, 16, 15, 'x', 17, 10],
    ['x', 'x', 'x', 5, 14, 9, 3, 15, 'x'],
    ['x', 6, 4, 'x', 'x', 'x', 18, 'x', 'x'],
    [17, 'x', 19, 'x', 1, 4, 'x', 8, 'x']
]

start, end = (2, 8), (6, 3)
matrix = [''.join(row) for row in matrix]
result = shortest_path(matrix, start, end)
print(result)
