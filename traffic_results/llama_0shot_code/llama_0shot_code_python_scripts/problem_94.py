
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc, matrix[nr][nc]

    heap = [(matrix[start[0]][start[1]], start)]
    visited = set()
    path = {}

    while heap:
        dist, (r, c) = heapq.heappop(heap)
        if (r, c) not in visited:
            visited.add((r, c))
            path[(r, c)] = dist

            if (r, c) == end:
                break

            for nr, nc, weight in get_neighbors(r, c):
                if (nr, nc) not in visited:
                    heapq.heappush(heap, (dist + weight, (nr, nc)))

    result = []
    r, c = end
    while (r, c) != start:
        result.append((r, c))
        dist = path[(r, c)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in path and path[(nr, nc)] == dist:
                r, c = nr, nc
                break
    result.append(start)
    result.reverse()

    return result

matrix = [
    ['x', 2, 'x', 12, 3, 8, 'x', 1, 5, 'x', 'x', 14, 'x', 5, 'x'],
    [5, 'x', 'x', 9, 19, 10, 10, 'x', 'x', 14, 16, 'x', 'x', 17, 'x'],
    [7, 4, 7, 18, 2, 7, 16, 'x', 7, 'x', 'x', 6, 'x'],
    [9, 'x', 14, 'x', 'x', 14, 7, 9, 'x', 'x', 14, 15, 14, 10, 13, 14, 8, 12, 11, 14],
    [8, 4, 'x', 17, 'x', 7, 15, 'x', 'x', 19, 'x', 10, 'x', 12, 13],
    [7, 11, 5, 6, 'x', 13, 'x', 'x', 15, 4, 9, 17, 19, 6, 8],
    [13, 'x', 'x', 'x', 'x', 'x', 'x', 4, 10, 'x', 7, 7, 17, 9],
    ['x', 'x', 6, 'x', 'x', 17, 12, 11, 'x', 'x', 'x', 10, 15, 14, 'x'],
    [16, 'x', 19, 'x', 'x', 4, 11, 16, 'x', 'x', 12, 'x', 'x'],
    ['x', 'x', 14, 'x', 'x', 19, 'x', 4, 13, 7, 'x', 'x', 'x', 'x', 8],
    ['x', 4, 'x', 13, 7, 14, 'x', 'x', 2, 15, 9, 11, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 19, 6, 2, 'x', 'x', 'x', 4, 7, 'x'],
    [17, 12, 10, 3, 5, 18, 'x', 'x', 'x', 11, 'x', 19, 13, 'x', 'x'],
    [1, 5, 'x', 17, 'x', 17, 7, 18, 'x', 'x', 8, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 2, 9, 10, 3, 'x', 'x', 15, 2, 'x']
]

start = (3, 2)
end = (7, 13)

result = dijkstra(matrix, start, end)
print(result)
