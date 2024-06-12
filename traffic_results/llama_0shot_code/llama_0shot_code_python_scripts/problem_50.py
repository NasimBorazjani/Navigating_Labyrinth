
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

    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    path = {start: None}

    while queue:
        dist, current = heapq.heappop(queue)
        if current not in visited:
            visited.add(current)
            if current == end:
                break
            for neighbor in get_neighbors(current[0], current[1]):
                if neighbor not in visited:
                    heapq.heappush(queue, (dist + matrix[neighbor[0]][neighbor[1]], neighbor))
                    path[neighbor] = current

    route = []
    while end is not None:
        route.append(end)
        end = path[end]
    route.reverse()

    return route

matrix = [
    [12, 17, 10, 'x', 'x', 'x', 'x', 9, 15, 5, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 12, 20, 9, 19, 8, 12, 11],
    [9, 'x', 'x', 2, 'x', 2, 1, 9, 8, 14, 16, 'x'],
    [19, 'x', 1, 20, 7, 9, 18, 'x', 18, 7, 'x', 'x'],
    [5, 2, 11, 9, 'x', 5, 4, 16, 'x', 1, 10],
    [10, 8, 8, 4, 11, 11, 'x', 'x', 5, 'x', 'x', 'x'],
    [15, 15, 'x', 'x', 13, 5, 19, 'x', 'x', 15, 'x', 'x'],
    [15, 16, 9, 18, 'x', 'x', 16, 'x', 'x', 'x', 5, 12],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 14, 14, 'x', 'x', 15, 6, 6, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 8, 14, 'x', 5, 'x', 'x', 15],
    ['x', 6, 15, 'x', 'x', 'x', 'x', 'x', 8, 'x', 'x']
]

start = (3, 9)
end = (7, 1)

route = shortest_path(matrix, start, end)
print(route)
