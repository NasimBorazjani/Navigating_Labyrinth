
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    graph = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                graph[(i, j)] = {}
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != 'x':
                        graph[(i, j)][(nx, ny)] = matrix[nx][ny]

    def district(i, j):
        if i <= 1: return 0
        if 2 <= i <= 5: return 1
        if 6 <= i <= 13: return 2

    dummy_nodes = {i: (rows + 1 + i, 0) for i in range(3)}
    for node in graph:
        dist = float('inf')
        prev = None
        for dnode in dummy_nodes.values():
            if dnode in graph[node]:
                ddist = graph[node][dnode]
                if ddist < dist:
                    dist = ddist
                    prev = dnode
        if prev is not None:
            graph[node][prev] = 0

    start, end = (6, 1), (3, 13)
    queue = [(0, start, [])]
    visited = set()
    while queue:
        dist, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[1:]
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor, path))

    return None

matrix = [
    'x', '5', '9', '6', '13', '13', '8', '6', '13', 'x', '13', 'x', 'x', 'x',
    '3', '10', '16', 'x', 'x', '3', '13', '1', '11', '9', '7', '6', 'x', '18',
    '9', '11', '3', 'x', 'x', '6', '13', 'x', '14', 'x', '12', '1', '2', '4',
    'x', '17', '13', 'x', '14', '4', '6', '8', 'x', 'x', '1', '12', 'x', '6', '2',
    '7', 'x', '11', 'x', '14', 'x', '11', '7', 'x', '5', 'x', '1', '12', 'x',
    'x', '20', '20', '19', 'x', '18', '2', '19', '1', '6', '12', 'x', 'x', '16',
    '8', '5', '7', '11', 'x', '1', 'x', 'x', 'x', '11', '4', 'x', 'x', '3',
    'x', '11', 'x', '11', '11', 'x', 'x', '18', 'x', 'x', 'x', '7', '6', 'x',
    '2', '2', '14', '5', '5', 'x', 'x', '11', '19', '16', 'x', '14', '7', '19',
    'x', '5', 'x', 'x', '7', 'x', '10', 'x', 'x', 'x', '3', '15', 'x', 'x',
    '19', 'x', 'x', 'x', 'x', '8', '3', '19', 'x', '18', 'x', 'x', 'x', 'x', 'x', '6', '6',
    'x', 'x', 'x', 'x', 'x', '4', 'x', 'x', '7', 'x', '6', 'x', '3'
]

print(shortest_path(matrix))
