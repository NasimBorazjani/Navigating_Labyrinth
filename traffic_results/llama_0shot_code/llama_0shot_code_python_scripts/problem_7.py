
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    district_ends = [1, 3, 5, 7]
    district_visited = [False]*4
    dist = {(i, j): float('inf') for i in range(height) for j in range(width)}
    dist[start] = 0
    prev = {(i, j): None for i in range(height) for j in range(width)}
    queue = [(0, start)]
    while queue:
        d, (r, c) = heapq.heappop(queue)
        if (r, c) == end:
            path = []
            while (r, c) is not None:
                path.append((r, c))
                r, c = prev[(r, c)]
            return path[::-1] # Reverse to get correct order
        if dist[(r, c)] < d:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and matrix[nr][nc] != 'x':
                new_dist = dist[(r, c)] + matrix[nr][nc]
                if new_dist < dist[(nr, nc)]:
                    dist[(nr, nc)] = new_dist
                    prev[(nr, nc)] = (r, c)
                    heapq.heappush(queue, (new_dist, (nr, nc)))
                    if nr // 3 in district_ends and not district_visited[nr // 3]:
                        district_visited[nr // 3] = True
                        path.append((nr, nc))
    return []

matrix = [
    ['x', 7, 7, 12, 7, 'x', 13, 1, 18],
    [9, 18, 'x', 4, 19, 8, 'x', 15, 10],
    [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'],
    [14, 4, 19, 9, 14, 'x', 'x', 7, 9],
    [9, 4, 11, 15, 7, 'x', 17, 3, 'x'],
    [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'],
    ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'],
    [3, 'x', 2, 'x', 'x', 'x', 'x', 4],
    ['x', 'x', 7, 'x', 19, 'x', 'x', 9]
]

start = (6, 1)
end = (2, 6)

result = dijkstra(matrix, start, end)
print(result)
