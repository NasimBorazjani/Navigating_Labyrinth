
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

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
    districts = {0: False, 1: False, 2: False}
    while queue:
        time, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end or all(visited for visited in districts.values()):
                return path[1:]  # Exclude start node from the path

            # Update districts
            if 0 <= node[0] <= 1:
                districts[0] = True
            elif 2 <= node[0] <= 5:
                districts[1] = True
            elif 6 <= node[0] <= 12:
                districts[2] = True

            for neighbor, cost in graph[node].items():
                heapq.heappush(queue, (time + cost, neighbor, path))

    return None  # No path found

matrix = [
    [18, 'x', 'x', 'x', 19, 'x', 'x', 'x'],
    ['x', 'x', 8, 1, 11, 'x', 'x', 'x', 'x', 4, 6, 4],
    [1, 4, 15, 13, 17, 11, 'x', 15, 'x', 13, 1, 'x', 'x'],
    [3, 'x', 6, 1, 15, 2, 'x', 13, 13, 'x', 'x', 'x', 'x'],
    [17, 12, 13, 11, 6, 1, 3, 'x', 'x', 19, 6, 6, 'x'],
    ['x', 17, 7, 12, 1, 15, 17, 20, 3, 'x', 'x', 18, 10],
    [16, 14, 15, 'x', 'x', 11, 'x', 17, 20, 15, 7, 10, 'x'],
    [5, 11, 'x', 7, 19, 'x', 6, 18, 15, 'x', 'x', 8, 'x', 1],
    [10, 'x', 1, 'x', 6, 'x', 11, 'x', 13, 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 4, 'x', 8, 'x', 12, 12, 13, 'x', 'x'],
    ['x', 'x', 18, 14, 'x', 'x', 5, 'x', 13, 1, 'x', 'x'],
    ['x', 'x', 1, 17, 8, 18, 'x', 7, 'x', 'x', 16, 8, 'x'],
    ['x', 'x', 'x', 16, 1, 19, 'x', 'x', 'x', 14, 'x', 'x']
]

start, end = (5, 12), (1, 2)
path = dijkstra(matrix, start, end)
print(path)
