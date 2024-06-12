
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    previous_nodes = [[None for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    districts_visited = [0, 0, 0]

    heap = [(0, start)]
    while heap:
        current_distance, (current_row, current_col) = heapq.heappop(heap)
        if (current_row, current_col) == end:
            path = []
            while (current_row, current_col) is not None:
                path.append((current_row, current_col))
                current_row, current_col = previous_nodes[current_row][current_col]
            return path[::-1]
        if visited[current_row][current_col]:
            continue
        visited[current_row][current_col] = True
        if current_row / 3 in [0, 1, 2] and districts_visited[current_row / 3] == 0:
            districts_visited[current_row / 3] = 1
        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] != 'x':
                distance = current_distance + matrix[new_row][new_col]
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    previous_nodes[new_row][new_col] = (current_row, current_col)
                    heapq.heappush(heap, (distance, (new_row, new_col)))
    return []

matrix = [
    ['x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'],
    ['x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2],
    ['x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'],
    [9, 3, 13, 8, 'x', 7, 'x', 4, 2, 'x'],
    [11, 17, 'x', 10, 'x', 'x', 'x', 17, 15, 11],
    ['x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7],
    ['x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9],
    [11, 'x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x'],
    ['x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7],
    [11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5],
    [9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10]
]

start, end = (7, 8), (2, 1)
path = dijkstra(matrix, start, end)
print(path)
