
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Convert matrix into graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, {start})]
    predecessor = {start: None}
    while queue:
        _, node, visited = heapq.heappop(queue)
        if node == end:
            break
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (weight, neighbor, visited | {neighbor}))
                predecessor[neighbor] = node

    # Retrieve path
    path = []
    while end is not None:
        path.append(end)
        end = predecessor.get(end)
    path.reverse()

    # Convert path into required format
    path = [(i, j) for i, j in path if matrix[i][j] != 'x']

    return path

matrix = [
    ['x', 'x', 7, 18, 11, 4, 9, 'x', 15, 'x', 'x', 'x', 1, 'x', 'x'],
    ['x', 'x', 14, 'x', 10, 'x', 'x', 8, 'x', 16, 1, 'x', 'x'],
    [17, 17, 'x', 'x', 'x', 'x', 'x', 7, 6, 12, 'x', 'x', 'x', 7, 'x'],
    # ...
    ['x', 13, 'x', 'x', 'x', 'x', 10, 5, 'x', 17, 'x', 'x', 7, 'x']
]

start, end = (7, 2), (4, 14)
path = dijkstra(matrix, start, end)
print(path)
