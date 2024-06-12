
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
    districts = {0: [], 1: [], 2: [], 3: []}
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                index = (i, j)
                graph[index] = []
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[index].append((matrix[i][j], (i-1, j)))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[index].append((matrix[i][j], (i, j-1)))
                if i < n-1 and matrix[i+1][j] != 'x':
                    graph[index].append((matrix[i][j], (i+1, j)))
                if j < m-1 and matrix[i][j+1] != 'x':
                    graph[index].append((matrix[i][j], (i, j+1)))
                if i < n-1 and j < m-1 and matrix[i+1][j+1] != 'x':
                    graph[index].append((matrix[i][j], (i+1, j+1)))
                if i > 0 and j < m-1 and matrix[i-1][j+1] != 'x':
                    graph[index].append((matrix[i][j], (i-1, j+1)))
                if i < n-1 and j > 0 and matrix[i+1][j-1] != 'x':
                    graph[index].append((matrix[i][j], (i+1, j-1)))
                if i > 0 and i < 4:
                    districts[0].append(index)
                elif i >= 4 and i < 7:
                    districts[1].append(index)
                elif i >= 7 and i < 9:
                    districts[2].append(index)
                else:
                    districts[3].append(index)

    start = (3, 1)
    end = (7, 8)
    cost, path = dijkstra(graph, start, end)
    visited_districts = set([i for i, j in path])
    for district in districts:
        if district not in visited_districts:
            end = districts[district][0]
            cost, path = dijkstra(graph, start, end)
            break

    return [(i, j) for i, j in path if matrix[i][j] != 'x']

matrix = [
    ['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
    ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
    ['x', 'x', 'x', 6, 'x', 13, 11, 1, 'x'],
    [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
    [14, 16, 'x', 'x', 'x', 'x', 'x', 18, 11],
    [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
    [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
    [4, 9, 6, 12, 13, 19, 'x', 14, 4],
    ['x', 'x', 17, 12, 7, 7, 9, 3, 1]
]

print(solve(matrix))
