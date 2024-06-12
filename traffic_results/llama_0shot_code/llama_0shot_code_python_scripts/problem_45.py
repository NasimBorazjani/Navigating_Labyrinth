
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    previous_nodes = [[None for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    queue = [(0, start)]
    while queue:
        current_distance, (current_row, current_col) = heapq.heappop(queue)
        if (current_row, current_col) == end:
            path = []
            while current_row is not None and current_col is not None:
                path.append((current_row, current_col))
                next_row, next_col = previous_nodes[current_row][current_col]
                current_row, current_col = next_row, next_col
            return path[::-1] # shortest path from start to end
        if not visited[current_row][current_col]:
            visited[current_row][current_col] = True
            for direction in directions:
                new_row, new_col = current_row + direction[0], current_col + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and matrix[new_row][new_col] != 'x':
                    distance = current_distance + matrix[new_row][new_col]
                    if distance < distances[new_row][new_col]:
                        distances[new_row][new_col] = distance
                        previous_nodes[new_row][new_col] = (current_row, current_col)
                        heapq.heappush(queue, (distance, (new_row, new_col)))
    return [] # if there is no path

matrix = [['x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1],
          ['x', 8, 'x', 'x', 'x', 18, 5, 1, 12, 14],
          [2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'],
          [17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13],
          ['x', 'x', 'x', 9, 17, 'x', 'x', 'x', 12, 17],
          ['x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8],
          [18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3],
          [4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6],
          [15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'],
          ['x', 'x', 'x', 4, 'x', 'x', 13, 'x', 'x', 'x'],
          ['x', 3, 'x', 'x', 'x', 'x', 1, 'x', 5, 13]]

start = (3, 10)
end = (6, 1)

print(dijkstra(matrix, start, end))
