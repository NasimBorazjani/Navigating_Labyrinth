
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Create a graph from the matrix
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)].append((matrix[i][j], (ni, nj)))

    # Use Dijkstra's algorithm to find the shortest path
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        dist, pos, path = heapq.heappop(queue)
        if pos not in visited:
            visited.add(pos)
            path = path + [pos]
            if pos == end:
                return path[::-1]  # reverse the path to start from the start workshop
            for d, next_pos in graph[pos]:
                heapq.heappush(queue, (dist + d, next_pos, path))

    # Check if it's possible to visit at least one workshop in each district
    districts = [(0, 3), (4, 5), (6, 9)]
    for d1, d2 in districts:
        if not any(d1 <= i <= d2 for i in path):
            return "Not possible to visit at least one workshop in each district"

    return "No path found"

matrix = [
    ['x', 16, 15, 14, 2, 12, 3, 'x', 7, 7],
    [11, 'x', 'x', 'x', 4, 10, 5, 'x', 'x', 'x'],
    [12, 'x', 3, 'x', 'x', 19, 13, 'x', 'x', 'x'],
    [16, 15, 13, 'x', 12, 'x', 'x', 1, 7],
    [2, 6, 'x', 5, 'x', 14, 7, 'x', 8, 18],
    [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
    [11, 1, 10, 11, 'x', 'x', 19, 6, 2, 18],
    [7, 'x', 10, 15, 'x', 'x', 'x', 'x', 18, 17],
    ['x', 6, 'x', 'x', 'x', 5, 'x', 7, 12, 20],
    ['x', 'x', 2, 15, 'x', 17, 'x', 'x', 10, 11]
]

print(dijkstra(matrix, (5, 0), (3, 9)))
