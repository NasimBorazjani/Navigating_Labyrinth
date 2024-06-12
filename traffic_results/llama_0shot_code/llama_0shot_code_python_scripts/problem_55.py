
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

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
    shortest_paths = {start: (None, matrix[start[0]][start[1]])}
    unvisited = [(matrix[start[0]][start[1]], start)]
    districts_visited = set()
    while unvisited and len(districts_visited) < 3:
        current_distance, current_node = heapq.heappop(unvisited)
        if current_node not in shortest_paths:
            continue
        for neighbor, distance in graph[current_node].items():
            district_visited = (neighbor[0] // 4) + 1  # Assuming rows = 12
            if district_visited not in districts_visited:
                districts_visited.add(district_visited)
            if neighbor not in shortest_paths or current_distance + distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, current_distance + distance)
                heapq.heappush(unvisited, (current_distance + distance, neighbor))

    # Backtrack to find the path
    path = []
    while end is not None:
        path.append(end)
        end = shortest_paths[end][0]
    path.reverse()

    return path

matrix = [
    [9, 4, 16, 7, 'x', 'x', 'x', 14, 'x', 'x', 'x'],
    ['x', 15, 10, 5, 12, 16, 'x', 'x', 'x', 3, 12, 18],
    [12, 'x', 'x', 'x', 9, 16, 3, 9, 'x', 'x', 'x', 7],
    [10, 6, 3, 10, 'x', 'x', 1, 17, 'x', 12, 12, 'x'],
    [11, 8, 15, 'x', 8, 16, 'x', 'x', 5, 15, 12, 7],
    ['x', 'x', 'x', 'x', 6, 'x', 11, 19, 17, 17, 10, 20],
    ['x', 3, 17, 17, 'x', 'x', 18, 'x', 'x', 9, 4],
    ['x', 1, 5, 17, 8, 15, 4, 17, 5, 6, 9, 11],
    ['x', 'x', 4, 5, 17, 18, 3, 'x', 9, 1, 11, 2],
    ['x', 'x', 5, 3, 4, 14, 14, 1, 17, 3, 12, 12],
    ['x', 15, 9, 7, 3, 'x', 'x', 'x', 'x', 'x', 17, 'x'],
    ['x', 'x', 13, 16, 6, 'x', 6, 'x', 'x', 'x', 'x', 'x']
]

print(dijkstra(matrix, (3, 9), (7, 1)))
