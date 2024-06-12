
import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return (cost, path)
            for c, neighbour in graph[node]:
                if neighbour not in seen:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")

def solve(matrix):
    graph = {}
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                if j < m - 1 and matrix[i][j + 1] != 'x':
                    graph[node].append((matrix[i][j + 1], (i, j + 1)))
                if j > 0 and matrix[i][j - 1] != 'x':
                    graph[node].append((matrix[i][j - 1], (i, j - 1)))
                if i < n - 1 and matrix[i + 1][j] != 'x':
                    graph[node].append((matrix[i + 1][j], (i + 1, j)))
                if i > 0 and matrix[i - 1][j] != 'x':
                    graph[node].append((matrix[i - 1][j], (i - 1, j)))
    start = (6, 0)
    end = (4, 9)
    cost, path = dijkstra(graph, start, end)
    return path[1:]

matrix = [
    [19, 'x', 7, 12, 15, 5, 19, 14],
    [17, 'x', 3, 5, 7, 'x', 'x', 'x', 17, 20],
    ['x', 11, 15, 8, 'x', 16, 4, 'x', 1, 1],
    ['x', 8, 19, 4, 3, 3, 3, 17, 8, 15],
    [13, 10, 17, 17, 6, 1, 'x', 8, 13, 20],
    [20, 'x', 'x', 'x', 'x', 4, 18, 4, 17, 'x'],
    [5, 'x', 'x', 10, 'x', 'x', 14, 2, 5, 'x'],
    [7, 'x', 4, 'x', 'x', 'x', 15, 'x', 'x', 'x'],
    [18, 'x', 18, 'x', 'x', 'x', 'x', 17, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x']
]

print(solve(matrix))
