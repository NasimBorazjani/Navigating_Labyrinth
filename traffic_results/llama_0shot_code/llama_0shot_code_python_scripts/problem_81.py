
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc, matrix[nr][nc]

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    start, end = (2, 0), (6, 11)
    queue = [(matrix[start[0]][start[1]], start)]
    distances = {start: 0}
    prev_node = {}

    while queue:
        dist, r, c = heapq.heappop(queue)
        if (r, c) == end:
            break
        for nr, nc, weight in get_neighbors(r, c):
            new_dist = dist + weight
            if (nr, nc) not in distances or new_dist < distances[(nr, nc)]:
                distances[(nr, nc)] = new_dist
                prev_node[(nr, nc)] = (r, c)
                heapq.heappush(queue, (new_dist + heuristic((nr, nc), end), nr, nc))

    path = []
    while (r, c) != start:
        path.append((r, c))
        r, c = prev_node[(r, c)]
    path.append(start)
    path.reverse()

    return path

matrix = [
    [8, 15, 3, 10, 6, 15, 'x', 'x', 'x', 'x', 'x', 4, 'x'],
    [3, 'x', 14, 8, 16, 19, 'x', 18, 4, 'x', 'x', 2, 'x'],
    [18, 18, 'x', 4, 'x', 17, 11, 10, 17, 9, 'x', 4, 1, 5],
    ['x', 2, 'x', 12, 1, 'x', 13, 17, 14, 15, 'x', 15, 'x'],
    ['x', 'x', 'x', 15, 'x', 2, 2, 11, 7, 'x', 5, 7, 4, 18],
    [16, 'x', 5, 'x', 19, 12, 5, 9, 13, 16, 9, 'x', 'x'],
    ['x', 'x', 'x', 'x', 14, 18, 'x', 16, 13, 'x', 1, 5, 10, 'x'],
    [3, 11, 'x', 1, 8, 'x', 'x', 'x', 18, 8, 11, 'x', 'x', 6],
    [19, 2, 'x', 19, 5, 'x', 'x', 'x', 9, 'x', 6, 'x', 4],
    ['x', 2, 'x', 10, 9, 15, 'x', 'x', 'x', 16, 'x', 8, 'x'],
    [18, 8, 10, 'x', 3, 'x', 11, 'x', 17, 'x', 17, 'x', 'x', 'x'],
    [14, 12, 'x', 2, 'x', 19, 2, 19, 14, 'x', 'x', 'x', 3, 'x'],
    [7, 'x', 'x', 'x', 'x', 'x', 9, 8, 7, 'x', 15, 2, 'x'],
    ['x', 'x', 15, 'x', 'x', 15, 16, 'x', 'x', 19, 'x', 13, 1]
]

print(shortest_path(matrix))
