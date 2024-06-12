
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
    nrows, ncols = len(matrix), len(matrix[0])
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < nrows and 0 <= y < ncols and matrix[x][y] != 'x':
                        graph[node].append((matrix[x][y], (x, y)))
    start, end = (2, 9), (5, 2)
    cost, path = dijkstra(graph, start, end)
    return path[1:]

matrix = [['x', 'x', 6, 'x', 'x', 'x', 15, 'x', 'x'],
          ['x', 17, 13, 13, 'x', 12, 3, 10, 2],
          ['x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2],
          ['x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'],
          ['x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'],
          [3, 'x', 3, 17, 8, 'x', 1, 16, 'x'],
          ['x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4],
          ['x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'],
          ['x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'],
          [1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5]]

print(solve(matrix))
