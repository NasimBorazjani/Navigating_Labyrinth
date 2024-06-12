
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
            for c, neighbor in graph[node]:
                heapq.heappush(queue, (cost + c, neighbor, path))
    return float("inf")

def solve(matrix):
    graph = {}
    districts = {0: [], 1: [], 2: [], 3: []}
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                index = (i, j)
                if i < 2:
                    districts[0].append(index)
                elif i < 5:
                    districts[1].append(index)
                else:
                    districts[2].append(index)
                districts[3].append(index)
                graph[index] = []
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] != 'x':
                        graph[index].append((matrix[x][y], (x, y)))

    start = (1, 8)
    end = (4, 1)
    cost, path = dijkstra(graph, start, end)
    visited_districts = {i: False for i in range(4)}
    for workshop in path:
        for i, district in enumerate(districts):
            if workshop in district:
                visited_districts[i] = True
    for i, visited in visited_districts.items():
        if not visited:
            nearest_workshop = min(districts[i], key=lambda w: abs(w[0]-start[0]) + abs(w[1]-start[1]))
            path.insert(path.index(nearest_workshop), start)
    return path

matrix = [
    [13, 'x', 'x', 'x', 'x', 8, 'x', 'x', 6],
    ['x', 'x', 'x', 8, 10, 'x', 17, 15, 14],
    ['x', 6, 'x', 'x', 'x', 16, 12, 7, 8, 11],
    ['x', 15, 'x', 1, 11, 19, 9, 17, 'x', 'x'],
    [18, 20, 16, 19, 12, 1, 'x', 'x', 'x', 5],
    [11, 'x', 18, 14, 'x', 2, 'x', 9, 8, 1],
    ['x', 2, 5, 16, 3, 9, 2, 18, 'x', 'x'],
    ['x', 8, 15, 17, 16, 6, 'x', 'x', 10],
    [3, 'x', 'x', 'x', 8, 9, 10, 'x', 'x', 6],
    [6, 'x', 9, 16, 1, 3, 16, 18, 'x', 'x']
]

print(solve(matrix))
