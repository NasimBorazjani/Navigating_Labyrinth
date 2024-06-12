
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

    # Convert matrix into graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        time, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[::-1]
            for neighbor, edge_time in graph[node].items():
                heapq.heappush(queue, (time + edge_time, neighbor, path))

    return None

matrix = [
    ['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3],
    ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17],
    [6, 16, 'x', 18, 10, 5, 'x', 'x', 'x', 7, 'x', 13, 12, 20],
    'x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13],
    [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 'x', 13, 12, 20],
    [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9],
    [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'],
    'x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'],
    [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'],
    [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'],
    'x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 'x'],
    [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']
]

# Flatten the matrix
matrix = [item for sublist in matrix for item in sublist]

# Find the shortest path
start, end = (8, 1), (5, 11)
path = shortest_path(matrix, start, end)
print(path)
