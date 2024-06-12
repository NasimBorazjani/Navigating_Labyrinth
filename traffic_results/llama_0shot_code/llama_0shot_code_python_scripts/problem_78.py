
import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for c, neighbour in graph[node]:
                heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")

def solve(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[node].append((matrix[ni][nj], (ni, nj)))
    start, end = (7, 12), (2, 0)
    cost, path = dijkstra(graph, start, end)
    return path

matrix = [
    ['x', 'x', 'x', 16, 11, 12, 'x', 'x', 17, 3, 'x', 'x', 4, 6],
    [4, 17, 'x', 'x', 3, 'x', 'x', 1, 9, 11, 12, 4, 'x', 'x'],
    [5, 'x', 'x', 7, 14, 4, 5, 7, 13, 4, 7, 'x', 'x', 'x'],
    [6, 6, 19, 3, 15, 'x', 'x', 'x', 'x', 4, 10, 19, 2, 4],
    [3, 16, 8, 'x', 5, 'x', 12, 17, 16, 'x', 9, 5, 6, 'x'],
    [17, 2, 'x', 'x', 16, 'x', 5, 'x', 'x', 5, 17, 7, 2, 5],
    [19, 'x', 'x', 'x', 2, 15, 15, 'x', 3, 11, 'x', 4, 'x'],
    ['x', 'x', 11, 'x', 'x', 17, 5, 'x', 'x', 'x', 19, 6, 'x'],
    [16, 17, 16, 'x', 12, 'x', 2, 18, 9, 7, 'x', 13, 'x', 'x'],
    [18, 11, 'x', 'x', 19, 5, 'x', 'x', 18, 4, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 2, 5, 4, 12, 3, 'x', 4, 14, 7, 19],
    [18, 'x', 'x', 'x', 7, 17, 'x', 3, 15, 'x', 16, 'x', 10],
    ['x', 11, 15, 'x', 'x', 'x', 'x', 2, 13, 'x', 'x', 'x', 3],
    [4, 8, 'x', 'x', 'x', 'x', 12, 13, 'x', 'x', 19, 'x', 6, 'x']
]

print(solve(matrix))
