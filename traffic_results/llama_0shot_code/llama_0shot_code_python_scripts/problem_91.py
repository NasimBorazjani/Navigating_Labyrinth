
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def get_neighbors(node):
        i, j = node
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width and matrix[ni][nj] != 'x':
                yield (ni, nj), matrix[ni][nj]

    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost, visited

            for neighbor, weight in get_neighbors(node):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))

    return None

def get_path(matrix, start, end):
    cost, visited = dijkstra(matrix, start, end)
    path = [end]
    while path[-1] != start:
        for node in visited:
            if node in path:
                path.insert(0, node)
                break
    return path

matrix = [
    ['x', 'x', 12, 'x', 18, 3, 2, 15, 6, 11, 13, 'x', 7, 17, 'x'],
    [13, 'x', 20, 13, 5, 2, 'x', 'x', 10, 12, 19, 19, 16, 'x', 17],
    [12, 12, 7, 'x', 'x', 'x', 9, 'x', 'x', 10, 10, 18, 4, 'x', 'x'],
    # ...
    ['x', 2, 'x', 14, 19, 'x', 4, 'x', 12, 4, 'x', 'x', 'x', 'x', 'x'],
    [16, 'x', 14, 'x', 6, 'x', 'x', 16, 'x', 9, 10, 18, 4],
    [3, 'x', 'x', 3, 'x', 'x', 'x', 9, 8, 'x', 9, 14, 'x', 14],
    ['x', 'x', 'x', 4, 19, 'x', 4, 15, 'x', 'x', 'x', 17, 'x', 'x'],
    [16, 17, 'x', 'x', 13, 'x', 18, 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'],
    ['x', 2, 17, 'x', 'x', 'x', 'x', 12, 3, 8, 'x', 2, 9],
    # ...
]

start = (5, 2)
end = (8, 14)

path = get_path(matrix, start, end)
print(path)
