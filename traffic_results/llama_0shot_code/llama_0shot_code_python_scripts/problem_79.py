
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    previous_nodes = [[None] * cols for _ in range(rows)]
    districts = {0: [], 1: [], 2: []}
    for i in range(3):
        districts[i] = [(i*5+j, k) for j in range(5) for k in range(5) if matrix[i*5+j][k] != 'x']
    queue = [(0, start)]
    while queue:
        current_distance, (current_row, current_col) = heapq.heappop(queue)
        if visited[current_row][current_col]:
            continue
        visited[current_row][current_col] = 1
        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and matrix[new_row][new_col] != 'x':
                distance = current_distance + matrix[new_row][new_col]
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    heapq.heappush(queue, (distance, (new_row, new_col)))
                    previous_nodes[new_row][new_col] = (current_row, current_col)
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous_nodes[current_node[0]][current_node[1]]
    path.reverse()
    return path

matrix = [
    ['x', 'x', 17, 7, 'x', 'x', 11, 4, 5, 15, 17, 6, 6, 2],
    [17, 'x', 'x', 6, 'x', 'x', 'x', 1, 8, 'x', 'x', 'x', 7],
    # more rows here...
    [9, 'x', 'x', 10, 13, 'x', 15, 1, 19]
]

start = (4, 12)
end = (7, 0)

path = dijkstra(matrix, start, end)
print(path)
