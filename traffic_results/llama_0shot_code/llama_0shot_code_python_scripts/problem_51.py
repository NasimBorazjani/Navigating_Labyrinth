
import heapq

def shortest_path(matrix):
    # Convert matrix into graph
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 'x':
                graph[(i, j)] = {}
                # Possible moves: up, down, left, right
                for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = i + x, j + y
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[i]) and matrix[nx][ny] != 'x':
                        graph[(i, j)][(nx, ny)] = matrix[nx][ny]

    # Use Dijkstra's algorithm to find shortest path
    queue = [(matrix[6][2], (6, 2))]  # (cost, node)
    visited = set()
    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == (2, 10):
                path = [node]
                while node != (6, 2):
                    for n, c in graph[node]:
                        if n in path:
                            node = n
                            path.append(node)
                            break
                path.reverse()
                return [(i, j) for i, j in path if matrix[i][j] != 'x']
            for n, c in graph[node]:
                heapq.heappush(queue, (cost + c, n))

    return []

matrix = [
    "19 12 x x 2 5 4 13 17 19 x 2".split(),
    "x 18 x 5 5 x x 8 12 18 x 15".split(),
    "x 9 4 10 7 20 x 16 20 13 15 x".split(),
    "8 x x 11 1 19 x 14 6 x 3 x".split(),
    "10 x 4 8 17 x 18 x 7 x 6 5".split(),
    "x x 3 1 8 18 x 4 17 x x 13".split(),
    "x x 6 x x x 14 x x 10 10 x".split(),
    "x x 15 x x x x x 2 x x x".split(),
    "x x 5 11 6 1 x 6 14 x x x".split(),
    "x 1 17 10 15 x 14 6 x x x x".split(),
    "12 2 x 10 x x 7 x x x x x".split(),
    "x 9 14 x 9 18 14 x x x 6 x".split()
]

for row in matrix:
    for i in range(len(row)):
        if row[i] == 'x':
            row[i] = 'x'
        else:
            row[i] = int(row[i])

print(shortest_path(matrix))
