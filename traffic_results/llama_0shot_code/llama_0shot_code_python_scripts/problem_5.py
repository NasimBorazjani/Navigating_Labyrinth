
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

def get_path(matrix, start, end):
    graph = {}
    districts = [[(i, j) for j, x in enumerate(row) if x != 'x' and x != 0] for i, row in enumerate(matrix) if row]
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x != 'x' and x != 0:
                node = (i, j)
                neighbors = [(matrix[i2][j2], (i2, j2)) for i2 in [i-1, i+1, i] for j2 in [j-1, j+1, j] if 0 <= i2 < len(matrix) and 0 <= j2 < len(row) and matrix[i2][j2] != 'x' and matrix[i2][j2] != 0 and (i2, j2) != node]
                graph[node] = neighbors
    cost, path = dijkstra(graph, start, end)
    return path

matrix = [
    [8, 'x', 7, 10, 'x', 12, 5, 'x'],
    ['x', 'x', 4, 11, 16, 4, 12, 15, 'x'],
    [3, 'x', 16, 16, 4, 'x', 'x', 'x'],
    [11, 6, 3, 12, 8, 2, 19, 14, 'x'],
    [20, 18, 19, 'x', 4, 18, 'x', 15, 13],
    [8, 15, 'x', 16, 11, 'x', 10, 14, 1],
    ['x', 'x', 'x', 19, 'x', 'x', 'x', 'x'],
    [7, 'x', 'x', 'x', 'x', 'x', 1, 7, 8],
    [15, 3, 'x', 'x', 'x', 'x', 'x', 'x']
]

print(get_path(matrix, (5, 0), (3, 7)))
