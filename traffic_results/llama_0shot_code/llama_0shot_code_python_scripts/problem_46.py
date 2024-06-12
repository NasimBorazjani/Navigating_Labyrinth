
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Convert the matrix into a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Run Dijkstra's algorithm
    start, end = (1, 0), (8, 10)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited_nodes = [(0, start)]

    while unvisited_nodes:
        current_distance, current_node = heapq.heappop(unvisited_nodes)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(unvisited_nodes, (distance, neighbor))

    # Backtrack to find the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    # Check and fix the path to visit all districts
    districts = {0: [], 1: [], 2: []}
    for i in range(len(path)):
        if path[i][0] < 2:
            districts[0].append(path[i])
        elif 2 <= path[i][0] < 8:
            districts[1].append(path[i])
        else:
            districts[2].append(path[i])

    for district in districts.values():
        if not district:
            for node in graph:
                if node not in path and distances[node] != float('infinity'):
                    district.append(node)
                    path.append(node)
                    break

    return path

matrix = [
    '3 14 2 x x x 19 13 17 12 8 x'.split(),
    '1 2 13 1 4 19 x x 16 x x 12'.split(),
    '9 8 9 15 x 12 x x x x x 14'.split(),
    '11 1 10 18 x 16 1 x 12 x x x'.split(),
    '7 16 13 10 13 x 14 x x 9 x 7'.split(),
    '19 7 7 20 13 14 18 x x 7 5 x'.split(),
    '4 x 11 x x 2 7 1 5 x x x'.split(),
    'x x x x x x x x 18 x 1 x'.split(),
    '4 x x 9 19 2 18 8 16 14 19 7'.split(),
    'x x x x 9 x 17 17 1 2 2 15'.split(),
    '18 x x x x x x 11 10 x 17 x'.split(),
    '9 x x x 10 3 x x 13 x 2 x'.split()
]

for row in matrix:
    for i in range(len(row)):
        if row[i] == 'x':
            row[i] = 'x'
        else:
            row[i] = int(row[i])

print(shortest_path(matrix))
