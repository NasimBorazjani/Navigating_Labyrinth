
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (3, 0), (6, 12)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    districts = [
        [(0, i), (0, i+1), (0, i+2)] for i in range(0, 14, 3)
    ]
    for district in districts:
        if not any(workshop in path for workshop in district):
            closest_workshop = min(district, key=lambda workshop: distances[workshop])
            path.insert(path.index(closest_workshop), closest_workshop)

    return path

matrix = [
    ['x', 6, 19, 13, 'x', 16, 11, 6, 14, 15, 7, 'x', 'x', 'x'],
    ['x', 6, 16, 15, 'x', 19, 16, 18, 'x', 8, 10, 'x', 'x', 'x'],
    ['x', 5, 10, 14, 2, 'x', 'x', 'x', 11, 'x', 'x', 'x', 'x'],
    [6, 13, 15, 10, 'x', 'x', 'x', 'x', 19, 'x', 'x', 'x', 2, 'x'],
    ['x', 15, 10, 6, 6, 8, 10, 9, 11, 'x', 'x', 'x', 16, 'x'],
    ['x', 'x', 'x', 8, 15, 12, 10, 19, 1, 18, 19, 4, 'x', 10],
    [1, 17, 'x', 'x', 6, 8, 4, 'x', 15, 8, 10, 6, 4, 'x'],
    ['x', 'x', 'x', 'x', 13, 'x', 5, 'x', 9, 10, 'x', 'x', 'x'],
    [12, 'x', 11, 'x', 13, 'x', 11, 7, 5, 13, 'x', 'x', 6, 15],
    ['x', 18, 19, 'x', 'x', 'x', 3, 'x', 16, 11, 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 2, 15, 'x', 8, 'x', 'x', 'x', 4, 11],
    [11, 'x', 6, 13, 12, 'x', 12, 'x', 9, 'x', 17, 'x', 'x'],
    ['x', 1, 18, 18, 3, 'x', 11, 13, 1, 13, 'x', 'x', 'x']
]

print(shortest_path(matrix))
