
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
                return path[::-1] # Reverse path to get correct order
            for neighbor, edge_time in graph[node].items():
                heapq.heappush(queue, (time + edge_time, neighbor, path))

    return None # No path found

# Test
matrix = [
    [18, 'x', 'x', 14, 5, 'x', 'x', 5, 18, 'x', 3, 'x'],
    ['x', 'x', 'x', 9, 2, 2, 'x', 15, 14, 12, 'x', 18],
    ['x', 'x', 3, 16, 3, 9, 'x', 16, 'x', 14, 'x', 17],
    ['x', 'x', 'x', 19, 7, 20, 'x', 'x', 11, 4, 'x', 4],
    [7, 'x', 8, 11, 'x', 1, 15, 5, 'x', 'x', 11, 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 6, 11, 'x', 'x', 'x', 8],
    ['x', 15, 2, 'x', 'x', 18, 'x', 1, 16, 15, 6, 5],
    ['x', 4, 18, 8, 9, 'x', 'x', 17, 20, 'x', 10],
    ['x', 16, 'x', 'x', 19, 'x', 17, 'x', 13, 11, 14, 2],
    [12, 'x', 11, 'x', 5, 3, 'x', 13, 17, 6],
    [14, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 11, 'x', 16],
    [12, 'x', 'x', 12, 'x', 10, 'x', 18, 14, 8, 'x']
]

start, end = (3, 3), (7, 11)
path = shortest_path(matrix, start, end)
print(path)
