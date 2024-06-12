
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (2, 0), (5, 6)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

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
    visited = {start: (None, matrix[start[0]][start[1]])}
    districts = {0: [], 1: [], 2: []}
    while queue:
        dist, (i, j) = heapq.heappop(queue)
        if (i, j) == end:
            path = [end]
            while (i, j) != start:
                i, j = visited[(i, j)]
                path.append((i, j))
            return path[::-1]

        for ni, nj in graph[(i, j)]:
            new_dist = dist + graph[(i, j)][(ni, nj)]
            if (ni, nj) not in visited or new_dist < visited[(ni, nj)][1]:
                heapq.heappush(queue, (new_dist, (ni, nj)))
                visited[(ni, nj)] = (i, j)

    # If the path doesn't visit all districts, add the remaining district with the shortest path
    for district in [0, 1, 2]:
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 'x' and (i, j) not in visited:
                    if i // 3 == district and (i // 3 * 3, j) in visited:
                        return shortest_path(matrix)  # Recursively find the shortest path again
