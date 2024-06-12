
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
                return (cost, path)
            for c, neighbour in graph[node]:
                if neighbour not in visited:
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
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[node].append((matrix[i-1][j], (i-1, j)))
                if i < rows - 1 and matrix[i+1][j] != 'x':
                    graph[node].append((matrix[i+1][j], (i+1, j)))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[node].append((matrix[i][j-1], (i, j-1)))
                if j < cols - 1 and matrix[i][j+1] != 'x':
                    graph[node].append((matrix[i][j+1], (i, j+1)))
    cost, path = dijkstra(graph, (1, 10), (7, 2))
    return path

matrix = [
    ['x', 'x', 8, 16, 3, 'x', 15, 17, 2, 'x', 'x', 5, 'x', 'x'],
    ['x', 'x', 17, 'x', 13, 'x', 13, 3, 3, 6, 11, 'x'],
    # ...
    ['x', 14, 'x', 'x', 3, 11, 12, 'x', 'x', 2, 6, 'x']
]

print(solve(matrix))
