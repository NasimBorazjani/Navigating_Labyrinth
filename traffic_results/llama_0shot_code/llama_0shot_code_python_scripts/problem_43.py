
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    # Convert the matrix into a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Initialize the dictionaries for distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    # Use a priority queue to select the node with the shortest known distance
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

    # Find the shortest path from the start node to the end node
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    # Check if the path visits at least one node in each district
    districts = [[(0, 3), (4, 5), (6, 10)], [(0, 3), (4, 5)], [(6, 10)]]
    for district in districts:
        if not any(node[0] in district[0] and node[1] in district[1] for node in path):
            # Add the shortest node from the district that is not visited to the path
            district_nodes = [node for node in graph if node[0] in district[0] and node[1] in district[1]]
            district_node = min(district_nodes, key=lambda node: distances[node])
            path.insert(path.index(max(path, key=lambda node: (node[0] not in district[0], node[1] not in district[1]))), district_node)

    return path

matrix = [
    ['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14],
    ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 9],
    [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15],
    ['x', 4, 'x', 'x', 18, 9, 'x', 15, 1, 9],
    [3, 2, 7, 'x', 'x', 17, 2, 14, 4, 2],
    [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7],
    ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4],
    ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'],
    ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'],
    ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'],
    ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]
]

start, end = (3, 10), (6, 2)
path = shortest_path(matrix, start, end)
print(path)
