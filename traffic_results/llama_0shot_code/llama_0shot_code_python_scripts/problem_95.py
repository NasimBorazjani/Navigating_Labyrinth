
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

def convert_to_graph(matrix):
    graph = {}
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = []
                if i > 0 and matrix[i-1][j] != 'x':
                    graph[node].append((matrix[i-1][j], (i-1, j)))
                if i < n-1 and matrix[i+1][j] != 'x':
                    graph[node].append((matrix[i+1][j], (i+1, j)))
                if j > 0 and matrix[i][j-1] != 'x':
                    graph[node].append((matrix[i][j-1], (i, j-1)))
                if j < m-1 and matrix[i][j+1] != 'x':
                    graph[node].append((matrix[i][j+1], (i, j+1)))
    return graph

def find_path(matrix, start, end):
    graph = convert_to_graph(matrix)
    shortest_path = dijkstra(graph, start, end)
    return shortest_path[1]

matrix = [
    ['x', 'x', 'x', 'x', 9, 14, 17, 'x', 13, 'x', 13, 10, 18],
    [1, 'x', 11, 12, 14, 13, 8, 'x', 5, 7, 'x', 'x', 'x', 'x'],
    [3, 'x', 'x', 18, 11, 16, 'x', 'x', 'x', 1, 15, 12, 10],
    # ...
    [19, 'x', 3, 'x', 'x', 7, 'x', 3, 16, 11, 'x', 17, 11, 1],
    ['x', 'x', 12, 16, 'x', 14, 9, 'x', 13, 1, 'x', 'x', 19],
    [15, 'x', 2, 8, 9, 13, 'x', 14, 'x', 6, 'x', 'x', 5]
]

start = (5, 2)
end = (9, 13)

print(find_path(matrix, start, end))
