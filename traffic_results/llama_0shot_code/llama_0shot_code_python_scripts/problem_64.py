
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    # Make a graph from the matrix
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    shortest_paths = {start: (0, [start])}
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, current_node)
                heapq.heappush(queue, (distance, neighbor))

    # Path from start to end
    path = end
    while path != start:
        path = shortest_paths[path][1]
    path = [path]

    # Ensure visiting at least one workshop in each district
    districts = [0, 4, 6, 12]
    for district in districts:
        if any(0 <= node[0] < district for node in path):
            for node in reversed(path):
                if 0 <= node[0] < district:
                    path.insert(0, node)
                    break
    return path

matrix = [
    [8, 'x', 12, 1, 'x', 'x', 7, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 16, 7, 8, 'x', 17, 19],
    [7, 'x', 13, 'x', 6, 14, 18, 'x', 19],
    [9, 20, 2, 10, 6, 'x', 18, 'x', 'x', 18, 13],
    ['x', 'x', 8, 12, 7, 14, 13, 9, 8, 6, 14, 11, 7],
    ['x', 14, 'x', 'x', 'x', 19, 13, 15, 3, 12, 16, 16, 3],
    ['x', 'x', 'x', 13, 9, 13, 10, 'x', 14, 'x', 4, 18],
    [6, 12, 10, 'x', 'x', 18, 7, 20, 18, 'x', 13, 1, 'x'],
    ['x', 5, 'x', 18, 12, 'x', 3, 12, 14, 19, 16, 'x'],
    [10, 'x', 19, 'x', 'x', 'x', 11, 14, 16, 12, 'x', 8],
    [8, 'x', 'x', 'x', 'x', 'x', 9, 16, 15, 'x', 'x', 8],
    ['x', 'x', 2, 1, 'x', 16, 'x', 3, 'x', 'x'],
    [9, 'x', 5, 'x', 15, 'x', 'x', 7, 15, 9, 'x']
]

print(dijkstra(matrix, (3, 0), (6, 12)))
