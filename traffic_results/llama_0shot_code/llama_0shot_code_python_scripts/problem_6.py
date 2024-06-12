
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc, matrix[nr][nc]

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        cost, position, path = heapq.heappop(queue)
        if position not in visited:
            visited.add(position)
            path = path + [position]
            if position == end:
                return path[::-1]  # Reverse path to get correct order
            for nr, nc, ncost in get_neighbors(position[0], position[1]):
                nposition = (nr, nc)
                if nposition not in visited:
                    heapq.heappush(queue, (cost + ncost + heuristic(nposition, end), nposition, path))
    return None

matrix = [
    [6, 16, 'x', 'x', 15, 'x', 14, 11, 'x'],
    [5, 2, 1, 'x', 3, 'x', 4, 13, 'x'],
    ['x', 7, 'x', 'x', 13, 'x', 10, 14, 5],
    [6, 16, 'x', 13, 6, 'x', 16, 'x', 'x'],
    ['x', 1, 17, 'x', 6, 3, 'x', 'x', 3],
    [11, 10, 7, 19, 15, 8, 12, 6, 'x'],
    [18, 'x', 'x', 9, 8, 9, 'x', 'x', 13],
    [4, 'x', 'x', 'x', 18, 20, 'x', 'x', 'x'],
    ['x', 'x', 8, 'x', 18, 2, 6, 13, 'x']
]

start = (5, 5)
end = (1, 0)

path = shortest_path(matrix, start, end)
print(path)
