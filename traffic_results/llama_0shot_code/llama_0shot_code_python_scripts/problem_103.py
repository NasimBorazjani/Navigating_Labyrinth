
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

def convert_to_graph(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 'x':
                        graph[node].append((matrix[x][y], (x, y)))
    return graph

matrix = [
    [6, 6, 2, 'x', 13, 'x', 'x', 'x', 11, 'x', 'x', 'x', 3, 'x'],
    [6, 11, 'x', 14, 'x', 'x', 1, 5, 6, 1, 19, 2, 7, 14],
    # ...
    [8, 'x', 5, 1, 7, 14, 'x', 'x', 'x', 14, 7, 'x', 8]
]

graph = convert_to_graph(matrix)
start, end = (2, 0), (6, 14)
cost, path = dijkstra(graph, start, end)
print(path)
