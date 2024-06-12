
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Represent the city as a graph
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)].append((matrix[ni][nj], (ni, nj)))

    # Initialize dictionaries to store shortest known distances and previous nodes
    shortest_distances = {node: float('inf') for row in matrix for node in row if node != 'x'}
    shortest_distances[start] = 0
    previous_nodes = {node: None for row in matrix for node in row if node != 'x'}

    # Use a priority queue to select the node with the shortest known distance
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > shortest_distances[current_node]:
            continue
        for edge_weight, neighbor in graph[current_node]:
            distance = current_distance + edge_weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Backtrack from the end node to find the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return path

matrix = [
    ['x', 'x', 10, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [6, 19, 'x', 'x', 'x', 12, 'x', 3, 'x', 'x', 'x'],
    [5, 3, 7, 7, 'x', 7, 9, 18, 'x', 'x', 'x'],
    [1, 4, 19, 19, 16, 6, 'x', 2, 10, 'x', 1, 7, 'x'],
    [14, 10, 'x', 'x', 2, 3, 5, 3, 13, 7, 'x', 8, 'x'],
    ['x', 8, 11, 14, 18, 'x', 'x', 16, 15, 8, 'x', 10, 'x'],
    ['x', 17, 'x', 15, 'x', 'x', 1, 17, 9, 7, 'x', 10, 'x'],
    [18, 6, 14, 4, 12, 12, 'x', 12, 5, 'x', 'x', 5, 18],
    ['x', 'x', 'x', 'x', 'x', 'x', 7, 17, 4, 16, 'x', 'x'],
    ['x', 6, 17, 'x', 'x', 'x', 'x', 15, 'x', 'x', 12, 'x'],
    [14, 'x', 'x', 12, 3, 11, 'x', 'x', 'x', 'x', 'x', 17],
    ['x', 16, 'x', 'x', 3, 5, 19, 16, 14, 'x', 'x', 19],
    [13, 'x', 'x', 3, 16, 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

start = (2, 3)
end = (8, 10)

path = dijkstra(matrix, start, end)
print(path)
