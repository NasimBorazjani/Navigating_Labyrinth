
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # north, south, west, east

    # Convert matrix to graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                break
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor))

    # Backtrack from the end node to the start node
    path = [end]
    while path[-1] != start:
        for node, weight in graph[path[-1]].items():
            if node not in visited or dist - weight != matrix[node[0]][node[1]]:
                continue
            path.append(node)
            break

    # Convert the path to the required format
    path = [(i, j) for i, j in reversed(path)]

    return path

matrix = [
    [16, 2, 16, 'x', 'x', 'x', 1, 16, 'x'],
    ['x', 'x', 19, 'x', 3, 5, 'x', 'x', 'x'],
    ['x', 'x', 'x', 3, 'x', 2, 'x', 10, 'x'],
    [11, 5, 20, 'x', 1, 3, 1, 'x', 9, 'x'],
    ['x', 'x', 8, 19, 'x', 'x', 'x', 16, 15],
    ['x', 3, 5, 10, 'x', 'x', 4, 1, 'x'],
    [9, 18, 10, 17, 5, 6, 'x', 'x', 'x', 5],
    ['x', 'x', 14, 5, 18, 'x', 'x', 1, 15, 1],
    [13, 'x', 13, 13, 14, 2, 19, 12, 'x', 1],
    [9, 6, 'x', 4, 12, 1, 13, 8, 2, 13]
]

start, end = (7, 9), (3, 2)
print(shortest_path(matrix, start, end))
