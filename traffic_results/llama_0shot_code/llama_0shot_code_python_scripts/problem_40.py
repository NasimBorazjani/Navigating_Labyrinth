
import heapq

def dijkstra(matrix, start, end, num_districts):
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
    shortest_paths = {start: (None, matrix[start[0]][start[1]])}
    unvisited = [(matrix[start[0]][start[1]], start)]
    visited_districts = set()

    while unvisited and len(visited_districts) < num_districts:
        current_distance, current_node = heapq.heappop(unvisited)

        if current_node not in shortest_paths:
            shortest_paths[current_node] = (previous_node, current_distance)
            visited_districts.add((current_node[0] // (rows // num_districts)) + 1)

        for neighbour, distance in graph[current_node].items():
            distance += current_distance
            if neighbour not in shortest_paths:
                heapq.heappush(unvisited, (distance, neighbour))

    # Reconstruct the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = shortest_paths[end][0]
    path.reverse()

    return path

matrix = [
    ['x', 10, 'x', 8, 13, 8, 4, 3, 'x', 17],
    [9, 'x', 6, 4, 'x', 16, 3, 19, 'x', 'x'],
    [8, 3, 18, 'x', 'x', 3, 'x', 7, 12, 16, 17],
    [8, 'x', 'x', 13, 'x', 7, 'x', 8, 'x', 12, 9],
    [2, 9, 'x', 'x', 9, 4, 18, 'x', 'x', 11, 'x'],
    [14, 20, 'x', 'x', 'x', 'x', 10, 'x', 'x', 7, 'x'],
    ['x', 'x', 18, 16, 12, 10, 'x', 'x', 10, 'x', 'x'],
    ['x', 'x', 16, 'x', 'x', 10, 'x', 3, 18, 18],
    ['x', 'x', 'x', 'x', 'x', 13, 3, 'x', 'x', 'x'],
    [5, 13, 1, 'x', 'x', 8, 'x', 19, 'x', 'x', 'x'],
    ['x', 'x', 16, 'x', 'x', 7, 18, 4, 11, 'x', 16]
]

start, end = (3, 10), (5, 1)
num_districts = 3

print(dijkstra(matrix, start, end, num_districts))
