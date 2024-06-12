
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # north, south, west, east

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, (r, c), path = heapq.heappop(queue)
        if (r, c) not in visited:
            visited.add((r, c))
            path = path + [(r, c)]
            if (r, c) == end:
                return path
            for nr, nc in get_neighbors(r, c):
                heapq.heappush(queue, (cost + matrix[nr][nc], (nr, nc), path))

    return None

def convert_to_matrix_indices(path):
    return [(i, j) for j, i in path]

matrix = [
    ['x', 9, 'x', 10, 'x', 11, 13, 5, 4, 'x', 'x', 19, 13, 'x', 'x'],
    ['x', 6, 3, 8, 18, 8, 1, 5, 2, 'x', 'x', 17, 'x', 'x', 'x'],
    ['x', 'x', 11, 5, 'x', 11, 13, 20, 7, 'x', 'x', 'x', 'x', 15, 4],
    ['x', 3, 'x', 14, 4, 20, 4, 15, 12, 12, 4, 'x', 8, 4, 'x'],
    [4, 1, 'x', 9, 17, 'x', 17, 'x', 11, 16, 6, 12, 'x', 18, 'x'],
    [8, 5, 17, 'x', 'x', 1, 'x', 'x', 'x', 19, 14, 2, 1, 'x', 'x'],
    [11, 9, 'x', 'x', 14, 'x', 'x', 'x', 'x', 'x', 2, 12, 4, 16],
    ['x', 'x', 2, 'x', 'x', 6, 6, 8, 'x', 11, 18, 11, 10, 'x', 'x'],
    ['x', 'x', 'x', 16, 'x', 7, 'x', 'x', 'x', 7, 11, 18, 9, 17],
    [13, 19, 13, 'x', 18, 'x', 14, 'x', 'x', 'x', 'x', 20, 15, 15],
    ['x', 'x', 'x', 'x', 17, 'x', 8, 'x', 'x', 'x', 'x', 6, 11, 'x'],
    [5, 'x', 7, 'x', 15, 'x', 'x', 'x', 10, 'x', 'x', 18],
    [11, 19, 'x', 18, 5, 'x', 19, 16, 'x', 13, 'x', 'x', 5],
    [8, 16, 6, 13, 1, 14, 4, 'x', 'x', 'x', 'x', 1, 'x', 'x', 5]
]

start = (8, 13)
end = (3, 3)

path = shortest_path(matrix, start, end)
path = convert_to_matrix_indices(path)

print(path)
