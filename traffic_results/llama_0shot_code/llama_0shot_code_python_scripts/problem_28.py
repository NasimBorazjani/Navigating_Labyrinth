
import heapq

def dijkstra(graph, start, end, districts):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if len(visited) == len(districts):
                return path
            for c, neighbour in graph[node]:
                if neighbour not in visited or neighbour in districts[len(path) % len(districts)]:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return None

def solve_problem(matrix):
    graph = {}
    districts = [{}, {}, {}]
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                if i < 4:
                    districts[0][(i, j)] = None
                elif i == 4:
                    districts[1][(i, j)] = None
                else:
                    districts[2][(i, j)] = None
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != 'x':
                        graph[(i, j)] = graph.get((i, j), []) + [(matrix[ni][nj], (ni, nj))]
    path = dijkstra(graph, (5, 0), (3, 8), districts)
    return [(i+1, j+1) for i, j in path]

matrix = [
    [15, 'x', 8, 6, 9, 'x', 'x', 'x', 'x'],
    [14, 'x', 8, 'x', 5, 11, 'x', 9],
    ['x', 17, 8, 'x', 17, 15, 12, 'x', 'x', 13],
    ['x', 13, 'x', 'x', 2, 17, 17, 1, 'x'],
    [6, 'x', 1, 5, 17, 'x', 18, 11, 7],
    [12, 8, 17, 10, 'x', 'x', 'x', 15, 'x', 16],
    [12, 12, 'x', 4, 'x', 13, 'x', 10, 'x', 16],
    ['x', 'x', 10, 'x', 'x', 'x', 'x', 8, 5],
    ['x', 2, 11, 18, 15, 'x', 11, 'x', 'x', 12],
    ['x', 'x', 14, 'x', 7, 14, 15, 18, 9]
]

print(solve_problem(matrix))
