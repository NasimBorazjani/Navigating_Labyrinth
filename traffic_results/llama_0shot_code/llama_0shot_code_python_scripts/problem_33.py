
import heapq

def shortest_path(matrix, start, end):
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
    queue = [(matrix[start[0]][start[1]], start)]
    shortest_distances = {start: 0}
    previous_nodes = {}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in shortest_distances or distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Backtrack to find the shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes.get(current_node)
    path.reverse()

    # Ensure that the path visits at least one workshop in each district
    districts = [range(0, 2), range(2, 5), range(5, 11)]
    district_workshops = [sorted([node for node in path if node[0] in district], key=lambda node: node[1]) for district in districts]
    final_path = []
    for workshops in district_workshops:
        if workshops:
            final_path.append(workshops[0])
    final_path.extend(path[final_path[-1]:])

    return final_path

matrix = [
    [16, 10, 'x', 16, 1, 12, 6, 12, 3, 7, 'x'],
    ['x', 16, 10, 9, 12, 19, 7, 10, 12, 13, 7],
    [5, 'x', 9, 'x', 5, 16, 16, 8, 'x', 16, 8],
    ['x', 4, 14, 'x', 'x', 'x', 'x', 'x', 7, 18],
    [13, 12, 16, 14, 'x', 2, 4, 2, 'x', 6, 3],
    ['x', 11, 20, 'x', 'x', 'x', 1, 'x', 'x', 9, 'x'],
    ['x', 'x', 8, 10, 'x', 'x', 3, 1, 'x', 'x', 6],
    ['x', 2, 9, 'x', 8, 13, 'x', 'x', 'x', 12, 11],
    [12, 'x', 2, 'x', 'x', 6, 'x', 15, 'x', 1],
    [3, 'x', 'x', 'x', 17, 'x', 18, 4, 1, 'x'],
    ['x', 'x', 6, 'x', 'x', 12, 'x', 'x', 15, 12]
]

start, end = (2, 10), (5, 2)
print(shortest_path(matrix, start, end))
