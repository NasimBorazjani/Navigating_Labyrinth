
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (3, 7), (5, 0)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Convert the matrix into a graph
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)].append((matrix[i][j], ni, nj))

    # Initialize the dictionary for distances and the set for unvisited nodes
    distances = {node: float('inf') for row in matrix for node in row if node != 'x'}
    distances[start] = 0
    unvisited = set(distances.keys()) - {start}

    # Use a priority queue to select the node with the shortest distance
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in unvisited:
            unvisited.remove(current_node)
            for distance, node_i, node_j in graph[current_node]:
                distance += current_distance
                if distance < distances[(node_i, node_j)]:
                    distances[(node_i, node_j)] = distance
                    heapq.heappush(queue, (distance, (node_i, node_j)))

    # Backtrack to find the shortest path
    path = [end]
    while path[-1] != start:
        for distance, node_i, node_j in graph[path[-1]]:
            if distance + distances[(node_i, node_j)] == distances[path[-1]]:
                path.append((node_i, node_j))
                break

    # Check and add the shortest path in each district if necessary
    districts = [(0, 3), (4, 4), (5, 8)]
    for d1, d2 in districts:
        if not any(i in range(d1, d2 + 1) for i, _ in path[1:-1]):
            for node_i, node_j in path[1:-1]:
                if node_i in range(d1, d2 + 1):
                    path.insert(1, (node_i, node_j))
                    break

    return path[::-1]  # Reverse the path to start from the start node

matrix = [
    ['x', 'x', 'x', 'x', '9', '20', '3', '9'],
    ['17', '11', '17', 'x', '9', '2', '7', 'x', '15'],
    ['x', '4', '2', '19', '12', '6', 'x', '4', '17'],
    ['15', 'x', 'x', '15', '11', '19', 'x', '9', '5'],
    ['3', '9', '19', '15', '2', 'x', 'x', '18', 'x'],
    ['19', '5', '9', '11', '9', 'x', 'x', '3', 'x'],
    ['x', 'x', '2', '8', '8', 'x', 'x', 'x', '19'],
    ['x', 'x', '14', 'x', 'x', 'x', '18', 'x', '18'],
    ['x', '14', '18', '7', '8', 'x', '10', '15', 'x']
]

print(shortest_path(matrix))
