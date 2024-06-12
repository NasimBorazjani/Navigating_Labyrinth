
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    dist = [[float('inf')] * width for _ in range(height)]
    prev = [[None] * width for _ in range(height)]
    visited = [[False] * width for _ in range(height)]
    district_visited = [False, False, False]
    district_workshops = [[(i, j) for j, val in enumerate(row) if val != 'x' and 4*i <= j < 4*(i+1)] for i, row in enumerate(matrix)]

    dist[start[0]][start[1]] = 0
    queue = [(0, start)]

    while queue:
        d, (r, c)) = heapq.heappop(queue)
        if visited[r][c]:
            continue
        visited[r][c] = True
        if r in range(4*start[0], 4*(start[0]+1)) and not district_visited[r//4]:
            district_visited[r//4] = True
            for dr, dc in district_workshops[r//4]:
                if not visited[dr][dc]:
                    heapq.heappush(queue, (dist[dr][dc], (dr, dc)))
        if (r, c) == end:
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc] and matrix[nr][nc] != 'x':
                new_dist = dist[r][c] + matrix[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    prev[nr][nc] = (r, c)
                    heapq.heappush(queue, (new_dist, (nr, nc)))

    path = []
    while end is not None:
        path.append(end)
        end = prev[end[0]][end[1]]
    path.reverse()

    return path, district_visited

matrix = [
    [16, 9, 19, 14, 16, 19, 6, 'x', 'x', 'x', 16, 18, 'x'],
    [19, 'x', 'x', 9, 9, 'x', 17, 16, 3, 'x', 'x', 14, 'x'],
    ['x', 'x', 11, 'x', 'x', 15, 15, 17, 10, 'x', 13, 5, 'x'],
    [2, 12, 9, 18, 7, 'x', 'x', 'x', 4, 'x', 10, 'x', 3],
    [8, 9, 19, 1, 4, 8, 'x', 17, 6, 'x', 18, 'x', 'x'],
    ['x', 6, 7, 9, 1, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 5, 4, 12, 13, 13, 'x', 'x', 'x', 11, 'x', 5, 9],
    ['x', 'x', 2, 20, 6, 11, 2, 'x', 'x', 'x', 10, 18, 'x'],
    ['x', 'x', 1, 18, 1, 17, 2, 3, 10, 12, 11, 'x', 19],
    ['x', 16, 'x', 'x', 16, 3, 10, 19, 'x', 'x', 9, 'x', 'x'],
    [10, 'x', 'x', 'x', 'x', 1, 10, 13, 'x', 'x', 13, 'x', 'x'],
    ['x', 'x', 'x', 'x', 13, 'x', 1, 14, 'x', 10, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 9, 2, 18, 19, 14, 10, 'x', 'x']
]

start = (3, 0)
end = (8, 9)

path, district_visited = dijkstra(matrix, start, end)

print(path)
