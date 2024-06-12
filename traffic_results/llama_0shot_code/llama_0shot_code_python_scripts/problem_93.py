
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

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

    # Retrieve the shortest path
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes.get(end)
    path.reverse()

    return path

matrix = [
    ['x', 'x', 'x', 'x', 2, 19, 'x', 'x', 15, 'x', 'x', 2, 17, 18, 18],
    # ... (the rest of the matrix)
    [4, 17, 5, 'x', 7, 5, 17, 12, 'x', 16, 8, 'x', 'x', 17, 'x']
]

start = (4, 14)
end = (7, 1)

path = shortest_path(matrix, start, end)
print(path)
