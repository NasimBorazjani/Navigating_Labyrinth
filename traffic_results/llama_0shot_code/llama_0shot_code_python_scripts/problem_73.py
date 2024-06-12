
import heapq

def shortest_path(matrix):
    # Convert matrix into graph
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 'x':
                node = (i, j)
                graph[node] = {}
                # North, South, West, East
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for n in neighbors:
                    if n[0] >= 0 and n[0] < len(matrix) and n[1] >= 0 and n[1] < len(matrix[i]) and matrix[n[0]][n[1]] != 'x':
                        graph[node][n] = matrix[n[0]][n[1]]

    # Dijkstra's algorithm
    queue = [(0, (3, 8), [])]  # (cost, node, path)
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == (8, 0):
                return path[::-1]  # Reverse path to get correct direction
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return None

matrix = [
    ['x', 14, 15, 10, 'x', 14, 'x', 'x', 18, 6, 'x', 'x', 4],
    [6, 'x', 'x', 'x', 1, 15, 'x', 2, 'x', 17, 'x'],
    ['x', 4, 'x', 17, 3, 14, 4, 2, 'x', 3, 'x', 11, 'x'],
    [6, 6, 'x', 19, 'x', 13, 'x', 6, 3, 'x', 'x'],
    [3, 10, 11, 'x', 'x', 4, 4, 1, 19, 'x', 'x', 'x', 17],
    [8, 'x', 'x', 8, 11, 18, 17, 18, 'x', 1, 1, 'x'],
    [14, 14, 1, 19, 6, 'x', 19, 19, 18, 9, 'x', 12, 18],
    [17, 6, 8, 'x', 1, 14, 19, 13, 'x', 'x', 9, 'x', 3],
    [16, 4, 'x', 'x', 'x', 9, 5, 'x', 'x', 'x', 18, 'x', 'x'],
    ['x', 'x', 10, 'x', 18, 'x', 1, 'x', 12, 9, 8, 3],
    ['x', 13, 17, 'x', 'x', 5, 8, 1, 'x', 1, 10, 'x'],
    [10, 11, 'x', 12, 'x', 6, 11, 'x', 9, 9, 15, 'x', 10],
    [5, 15, 1, 8, 5, 'x', 6, 'x', 9, 18, 'x', 'x']
]

print(shortest_path(matrix))
