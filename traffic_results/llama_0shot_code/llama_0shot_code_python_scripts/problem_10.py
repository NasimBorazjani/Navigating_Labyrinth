
import heapq

def dijkstra(graph, start, end, num_districts):
    queue = [(0, start, [])]
    visited = set()
    districts_visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if len(districts_visited) == num_districts - 1 and node != end:
                continue
            districts_visited.add(node[1] // 4)
            if node == end:
                return path
            for c, neighbour in graph[node]:
                heapq.heappush(queue, (cost + c, neighbour, path))
    return None

def solve(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    graph = {}
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < num_rows and 0 <= y < num_cols and matrix[x][y] != 'x':
                        graph[node].append((matrix[x][y], (x, y)))
    start, end = (3, 0), (6, 6)
    path = dijkstra(graph, start, end, 3)
    return path

matrix = [['x', 'x', 6, 'x', 7, 9, 4, 11],
          ['x', 3, 'x', 6, 5, 3, 15, 'x', 3],
          ['x', 'x', 'x', 4, 'x', 9, 1, 8, 'x'],
          [15, 18, 1, 6, 5, 10, 6, 14, 8],
          [18, 10, 7, 18, 2, 'x', 'x', 'x', 7],
          [11, 9, 16, 'x', 11, 'x', 11, 'x', 17],
          [7, 'x', 18, 'x', 10, 20, 6, 'x'],
          [15, 4, 17, 'x', 16, 2, 12, 16, 'x'],
          [9, 10, 18, 17, 9, 6, 7, 'x', 15]]

print(solve(matrix))
