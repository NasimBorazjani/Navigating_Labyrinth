
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path
            for neighbor in get_neighbors(*node):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + matrix[neighbor[0]][neighbor[1]], neighbor, path))

    return None

matrix = [
    ['x', 10, 16, 12, 'x', 'x', 'x', 'x', 18, 18, 10, 'x', 'x', 19],
    [7, 'x', 'x', 11, 5, 13, 6, 'x', 'x', 'x', 'x', 'x', 8, 14],
    # ...
    ['x', 1, 7, 'x', 'x', 'x', 9, 16, 9, 16, 'x', 11, 'x', 9],
    # ...
]

start, end = (9, 10), (2, 3)
path = shortest_path(matrix, start, end)
print(path)
