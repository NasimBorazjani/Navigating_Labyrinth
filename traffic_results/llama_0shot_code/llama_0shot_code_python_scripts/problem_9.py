
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
            for (next_node, edge_cost) in graph[node]:
                if next_node not in seen:
                    heapq.heappush(queue, (cost + edge_cost, next_node, path))
    return float("inf")

def solve(matrix):
    graph = {}
    districts = [[(i, j) for j, cell in enumerate(row) if cell != 'x'] for i, row in enumerate(matrix)]
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell != 'x':
                workshop = (i, j)
                if workshop != (4, 0):  # We don't need to add an edge to the destination
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(matrix) and 0 <= ny < len(districts[0]) and matrix[nx][ny] != 'x':
                            next_workshop = (nx, ny)
                            edge_cost = matrix[nx][ny]
                            if workshop not in graph:
                                graph[workshop] = []
                            graph[workshop].append((next_workshop, edge_cost))
    cost, path = dijkstra(graph, (1, 8), (4, 0))
    return [(i, j) for i, j in path if i in range(len(districts)) and j in range(len(districts[0]))]

matrix = [
    [6, 9, 19, 'x', 5, 9, 'x', 15, 'x'],
    [8, 10, 16, 'x', 'x', 'x', 5, 11, 4],
    [5, 11, 20, 1, 14, 16, 7, 1, 5],
    [10, 5, 3, 5, 12, 8, 'x', 'x', 2],
    [16, 15, 15, 14, 'x', 13, 10, 'x', 10],
    [6, 4, 7, 13, 'x', 'x', 'x', 'x', 13],
    ['x', 1, 6, 3, 'x', 'x', 17, 9, 5],
    ['x', 11, 'x', 9, 'x', 5, 7, 'x'],
    ['x', 'x', 'x', 18, 'x', 2, 'x', 'x', 12]
]

print(solve(matrix))
