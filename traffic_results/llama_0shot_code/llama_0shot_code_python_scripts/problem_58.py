
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

def convert_to_graph(matrix):
    graph = {}
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[node].append((matrix[i-1][j], (i-1, j)))
                if i < n-1 and matrix[i+1][j] != 'x':
                    graph[node].append((matrix[i+1][j], (i+1, j)))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[node].append((matrix[i][j-1], (i, j-1)))
                if j < m-1 and matrix[i][j+1] != 'x':
                    graph[node].append((matrix[i][j+1], (i, j+1)))
    return graph

matrix = [
    ['x', 'x', 'x', 6, 9, 'x', 'x', 10, 7, 3, 12],
    ['x', 11, 'x', 3, 14, 16, 17, 1, 4, 14, 8, 16],
    [3, 'x', 'x', 'x', 6, 1, 18, 16, 'x', 6, 3, 11],
    ['x', 'x', 11, 4, 8, 'x', 'x', 1, 3, 9, 8, 7],
    ['x', 'x', 3, 'x', 'x', 'x', 8, 14, 18, 'x', 'x', 18],
    [4, 1, 'x', 'x', 'x', 14, 'x', 'x', 3, 4, 20],
    [1, 'x', 'x', 'x', 14, 19, 15, 'x', 'x', 3, 16, 15],
    ['x', 'x', 6, 18, 'x', 'x', 16, 1, 3, 'x', 11],
    ['x', 3, 'x', 15, 'x', 19, 10, 'x', 'x', 'x', 'x', 'x'],
    ['x', 9, 'x', 'x', 'x', 17, 17, 'x', 16, 'x', 13],
    ['x', 'x', 8, 'x', 'x', 1, 'x', 'x', 19, 19, 1],
    ['x', 3, 9, 'x', 'x', 'x', 1, 3, 10, 11, 8]
]

graph = convert_to_graph(matrix)
start = (1, 3)
end = (6, 10)
cost, path = dijkstra(graph, start, end)
print(path)
