
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north, east, south, west

    # Represent the matrix as a graph
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)].append((matrix[i][j], ni, nj))

    # Initialize the shortest distances and previous nodes
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    # Use a priority queue to select the node with the shortest distance
    queue = [(0, start)]
    while queue:
        current_distance, (i, j) = heapq.heappop(queue)
        if (i, j) == end:
            break
        if current_distance > distances[(i, j)]:
            continue
        for distance, ni, nj in graph[(i, j)]:
            new_distance = current_distance + distance
            if new_distance < distances[(ni, nj)]:
                distances[(ni, nj)] = new_distance
                previous_nodes[(ni, nj)] = (i, j)
                heapq.heappush(queue, (new_distance, (ni, nj)))

    # Reconstruct the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path = path[::-1]

    # Ensure visiting at least one workshop in each district
    districts = [set(range(0, 3), set(range(3, 8)), set(range(8, 12)))]
    district_counts = {d: 0 for d in districts}
    for node in path:
        district_counts[districts[node[0] // 3]] += 1
    for d, count in district_counts.items():
        if count == 0:
            # Add the nearest workshop in the district to the path
            for node in sorted(graph.keys(), key=lambda x: abs(x[0] - d.start) + abs(x[1] - d.end)):
                if node not in path:
                    path.append(node)
                    break

    return path

matrix = [
    [10, 'x', 'x', 1, 1, 'x', 'x', 'x', 'x', 'x', 'x'],
    [11, 9, 17, 'x', 14, 3, 'x', 13, 'x', 'x', 6, 'x'],
    ['x', 5, 'x', 'x', 10, 13, 19, 10, 'x', 1, 12],
    [6, 'x', 'x', 17, 5, 6, 17, 4, 5, 'x', 1, 'x'],
    [4, 11, 1, 'x', 'x', 'x', 14, 7, 19, 4, 'x', 6],
    ['x', 'x', 6, 18, 'x', 'x', 'x', 5, 8, 2, 1, 'x'],
    [19, 19, 10, 9, 19, 19, 'x', 6, 'x', 1, 14, 11],
    ['x', 'x', 'x', 18, 11, 'x', 7, 5, 15, 13, 1, 11],
    ['x', 4, 'x', 'x', 11, 'x', 'x', 'x', 'x', 15],
    [10, 8, 10, 2, 'x', 'x', 'x', 'x', 'x', 12, 'x', 17],
    [19, 'x', 3, 11, 'x', 9, 3, 15, 'x', 5, 8, 17],
    [18, 'x', 'x', 11, 14, 'x', 14, 13, 'x', 'x', 8]
]

start = (3, 3)
end = (8, 11)

path = dijkstra(matrix, start, end)
print(path)
