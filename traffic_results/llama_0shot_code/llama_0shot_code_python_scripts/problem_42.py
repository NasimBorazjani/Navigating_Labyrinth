
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (6, 10), (3, 2)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    # Convert matrix to graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start)]
    visited = {start: (None, matrix[start[0]][start[1]])}
    districts_visited = {1: False, 2: False, 3: False}
    while queue:
        _, current = heapq.heappop(queue)
        if current == end:
            path, _ = current_district = visited[current]
            while path is not None:
                path, district = visited[path]
                if district is not None:
                    districts_visited[district] = True
                current_district = path, district
            if all(value for value in districts_visited.values()):
                return list(current_district)[::-1]
        for neighbor, cost in graph[current].items():
            if neighbor not in visited or visited[neighbor][1] > visited[current][1] + cost:
                heapq.heappush(queue, (visited[neighbor][1] = visited[current][1] + cost, neighbor))
                visited[neighbor] = current, visited[current][0]
    return None

matrix = [
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
]

print(shortest_path(matrix))
