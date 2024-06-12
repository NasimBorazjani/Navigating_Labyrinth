
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    # Convert the matrix into a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Apply Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        time, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[::-1]  # Reverse the path to get the correct order
            for neighbor, edge_time in graph[node].items():
                heapq.heappush(queue, (time + edge_time, neighbor, path))

    return None  # No path found

# Test the function
matrix = [
    ['x', 12, 8, 4, 4, 16, 8, 'x', 'x', 17, 18, 9, 'x', 16],
    [2, 9, 'x', 1, 4, 13, 20, 11, 2, 'x', 11, 7, 14, 12],
    ['x', 'x', 'x', 'x', 17, 15, 8, 12, 'x', 'x', 7, 'x', 'x'],
    [2, 2, 'x', 5, 14, 'x', 1, 5, 4, 14, 7, 'x', 'x'],
    [19, 'x', 11, 1, 19, 19, 12, 'x', 12, 13, 5, 3, 17, 17],
    ['x', 'x', 'x', 'x', 'x', 1, 'x', 4, 'x', 'x', 8, 'x', 'x'],
    [6, 'x', 10, 'x', 7, 1, 11, 'x', 'x', 3, 'x', 'x', 'x'],
    [19, 'x', 3, 11, 'x', 6, 11, 12, 14, 10, 'x', 11, 18],
    [13, 'x', 'x', 'x', 'x', 'x', 4, 'x', 'x', 'x', 'x', 10, 5],
    [19, 'x', 'x', 16, 'x', 18, 'x', 8, 'x', 2, 11, 'x', 'x'],
    ['x', 14, 'x', 6, 'x', 18, 11, 14, 11, 2, 'x', 'x'],
    ['x', 'x', 6, 8, 10, 8, 14, 'x', 'x', 13, 'x', 10, 'x'],
    ['x', 19, 'x', 7, 12, 17, 'x', 15, 'x', 16, 1, 'x', 'x'],
    [8, 'x', 17, 'x', 5, 15, 'x', 16, 1, 'x', 'x', 17, 'x']
]

start, end = (4, 3), (8, 13)
path = shortest_path(matrix, start, end)
print(path)
