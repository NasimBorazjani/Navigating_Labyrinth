
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up

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
                return path[::-1] # Reverse path to get correct order
            for neighbor, edge_time in graph[node].items():
                heapq.heappush(queue, (time + edge_time, neighbor, path))

    return None # No path found

# Test
matrix = [
    [15, 8, 18, 3, 19, 'x', 17, 'x', 'x', 'x', 'x'],
    [19, 16, 'x', 18, 20, 5, 7, 11, 12, 3],
    [18, 'x', 18, 1, 2, 'x', 'x', 12, 16, 4],
    [9, 20, 4, 19, 5, 15, 'x', 'x', 'x', 6, 4],
    ['x', 18, 8, 1, 'x', 7, 1, 7, 10, 1, 4],
    ['x', 18, 'x', 18, 19, 9, 18, 5, 15, 1, 7],
    [3, 'x', 12, 14, 'x', 'x', 'x', 1, 'x', 'x'],
    ['x', 12, 6, 'x', 6, 'x', 1, 1, 7, 'x'],
    ['x', 5, 10, 14, 2, 'x', 'x', 7, 11, 3, 'x'],
    [6, 9, 13, 'x', 'x', 'x', 'x', 'x', 'x', 3],
    [19, 12, 'x', 15, 'x', 14, 'x', 'x', 19]
]

start, end = (3, 1), (5, 10)
print(shortest_path(matrix, start, end))
