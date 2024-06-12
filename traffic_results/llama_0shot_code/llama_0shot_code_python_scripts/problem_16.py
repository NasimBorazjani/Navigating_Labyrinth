
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
                heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")

def solve(matrix):
    graph = {}
    districts = [[(i, j) for j, x in enumerate(row) if x != 'x' and x != 0] for i, row in enumerate(matrix) if i % 4 < 3]
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x != 'x':
                if i > 0 and matrix[i - 1][j] != 'x':
                    graph[(i, j)] = [(x, (i - 1, j))]
                if j > 0 and matrix[i][j - 1] != 'x':
                    graph[(i, j)] = [(x, (i, j - 1))]
                if i < len(matrix) - 1 and matrix[i + 1][j] != 'x':
                    graph[(i, j)] = [(x, (i + 1, j))]
                if j < len(row) - 1 and matrix[i][j + 1] != 'x':
                    graph[(i, j)] = [(x, (i, j + 1))]
    cost, path = dijkstra(graph, (5, 1), (3, 9))
    districts_visited = set(i // 4 for i in path)
    penalty = sum(i not in districts_visited for i in range(3)) * 1000
    return cost + penalty, path

matrix = [
    ['x', 'x', 'x', 16, 1, 13, 17, 7, 14, 'x'],
    ['x', 10, 'x', 12, 'x', 13, 'x', 8, 19, 4],
    [9, 13, 'x', 13, 'x', 'x', 15, 'x', 16],
    [3, 8, 'x', 16, 12, 'x', 'x', 'x', 13],
    [13, 'x', 1, 15, 18, 8, 'x', 10, 'x', 'x'],
    [8, 1, 2, 14, 'x', 8, 'x', 4, 'x', 11],
    [14, 13, 15, 'x', 16, 'x', 13, 'x', 19],
    ['x', 4, 10, 'x', 'x', 16, 'x', 11, 'x', 'x'],
    ['x', 14, 'x', 'x', 'x', 'x', 18, 6, 18],
    ['x', 3, 2, 6, 7, 'x', 'x', 9, 8, 5]
]

print(solve(matrix))
