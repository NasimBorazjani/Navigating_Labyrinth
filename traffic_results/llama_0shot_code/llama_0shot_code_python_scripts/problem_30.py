
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
                graph[(i, j)] = []
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 'x':
                        graph[(i, j)].append((matrix[x][y], (x, y)))
    cost, path = dijkstra(graph, (4, 9), (6, 1))
    return path[1:]

matrix = [
    [8, 'x', 'x', 9, 15, 13, 11, 2, 'x', 'x'],
    [13, 'x', 'x', 'x', 5, 'x', 7, 'x', 'x'],
    [12, 3, 'x', 'x', 'x', 'x', 'x', 10, 'x', 'x'],
    [12, 'x', 'x', 9, 15, 9, 11, 5, 17, 'x'],
    [3, 5, 12, 'x', 11, 5, 'x', 15, 1, 18],
    [14, 3, 'x', 'x', 18, 14, 19, 19, 12, 15],
    ['x', 20, 17, 15, 11, 'x', 'x', 'x', 'x', 'x'],
    [12, 13, 18, 'x', 'x', 5, 'x', 2, 13],
    ['x', 'x', 13, 19, 4, 'x', 12, 'x', 'x', 8],
    ['x', 'x', 10, 'x', 'x', 'x', 15, 'x', 4, 16]
]

print(solve(matrix))
