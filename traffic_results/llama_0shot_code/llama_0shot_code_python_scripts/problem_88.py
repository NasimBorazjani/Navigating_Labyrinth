
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (3, 1), (5, 13)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def neighbors(i, j):
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                yield ni, nj

    graph = {(i, j): list(neighbors(i, j)) for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    distances[start] = 0
    previous_nodes = {}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor in graph[current_node]:
            distance = current_distance + matrix[neighbor[0]][neighbor[1]]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes.get(end)
    path.reverse()

    return path

matrix = [
    ['x', 7, 'x', 13, 8, 2, 15, 2, 5, 15, 6, 4, 7, 'x'],
    ['x', 6, 19, 17, 5, 13, 15, 2, 11, 5, 'x', 'x', 9, 8],
    [16, 12, 10, 7, 8, 19, 19, 9, 5, 10, 2, 'x', 'x', 12],
    ['x', 1, 19, 20, 'x', 3, 4, 18, 'x', 'x', 10, 1, 12, 2],
    ['x', 1, 4, 1, 1, 10, 4, 'x', 12, 'x', 5, 10, 3, 8],
    ['x', 'x', 'x', 7, 'x', 'x', 16, 12, 'x', 'x', 'x', 13, 6, 10],
    ['x', 'x', 11, 12, 13, 15, 8, 'x', 12, 1, 16, 14, 8, 15],
    ['x', 11, 'x', 15, 'x', 'x', 'x', 'x', 5, 'x', 'x', 14],
    [1, 'x', 'x', 8, 'x', 13, 17, 'x', 3, 12, 'x', 'x', 'x'],
    [14, 3, 'x', 'x', 'x', 'x', 12, 'x', 7, 'x', 'x', 'x'],
    ['x', 5, 15, 'x', 10, 17, 'x', 6, 9, 2, 'x', 'x', 'x'],
    [1, 7, 17, 1, 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x', 12],
    ['x', 'x', 14, 18, 8, 19, 19, 16, 'x', 6, 5, 16, 17, 7],
    ['x', 'x', 'x', 'x', 'x', 'x', 19, 17, 'x', 2, 12, 'x', 'x']
]

print(shortest_path(matrix))
