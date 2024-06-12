
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (7, 0), (3, 8)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Convert matrix to graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        dist, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[1:]  # exclude start node
            for neighbor, cost in graph[node].items():
                heapq.heappush(queue, (dist + cost, neighbor, path))

    return None

matrix = [
    ['x', 11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14],
    ['x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'],
    ['x', 8, 1, 5, 17, 'x', 4, 8, 20, 7, 4],
    ['x', 10, 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'],
    [18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'],
    [5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18],
    [19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'],
    [15, 5, 7, 14, 6, 'x', 'x', 'x', 13, 'x'],
    [18, 7, 'x', 19, 12, 'x', 'x', 15, 'x', 'x'],
    [10, 9, 'x', 1, 'x', 15, 'x', 11, 'x', 2],
    ['x', 'x', 8, 'x', 19, 1, 'x', 'x', 8, 'x']
]

print(shortest_path(matrix))
