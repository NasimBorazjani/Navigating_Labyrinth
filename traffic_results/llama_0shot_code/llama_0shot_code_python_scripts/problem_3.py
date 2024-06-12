
import heapq

def dijkstra(graph, start, end, districts):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path
            for c, neighbour in graph[node]:
                if neighbour not in visited and neighbour[0] in districts[node[0]]:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return None

def solve(matrix):
    graph = {}
    districts = {}
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                if i <= 1:
                    districts[(i, j)] = 1
                elif 2 <= i <= 6:
                    districts[(i, j)] = 2
                else:
                    districts[(i, j)] = 3

                if i < n - 1 and matrix[i + 1][j] != 'x':
                    graph[(i, j)] = [(matrix[i][j], (i + 1, j))]
                if i > 0 and matrix[i - 1][j] != 'x':
                    graph[(i, j)] = [(matrix[i][j], (i - 1, j))]
                if j < m - 1 and matrix[i][j + 1] != 'x':
                    graph[(i, j)] = [(matrix[i][j], (i, j + 1))]
                if j > 0 and matrix[i][j - 1] != 'x':
                    graph[(i, j)] = [(matrix[i][j], (i, j - 1))]

    path = dijkstra(graph, (7, 7), (1, 2), districts)
    return path

matrix = [
    [10, 14, 4, 16, 'x', 17, 5, 'x', 'x'],
    [5, 20, 16, 3, 1, 8, 'x', 16, 19],
    [1, 'x', 5, 13, 3, 15, 19, 15, 'x'],
    ['x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'],
    ['x', 16, 'x', 17, 11, 1, 'x', 15, 'x'],
    [10, 'x', 14, 11, 5, 7, 12, 'x', 5],
    [7, 'x', 15, 'x', 15, 8, 3, 6, 7],
    ['x', 12, 14, 'x', 'x', 'x', 16, 3, 13],
    [19, 5, 10, 'x', 'x', 'x', 9, 7, 14]
]

print(solve(matrix))
