
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # north, south, west, east
    visited = [[0 for _ in range(width)] for _ in range(height)]
    previous_node = [[None for _ in range(width)] for _ in range(height)]
    queue = [(matrix[start[0]][start[1]], start)]
    district_visited = {1: False, 2: False, 3: False}

    while queue:
        path_len, current = heapq.heappop(queue)
        if visited[current[0]][current[1]]:
            continue
        visited[current[0]][current[1]] = 1

        if current[0] in [0, 1, 2] and not district_visited[1]:
            district_visited[1] = True
        elif current[0] in [3, 4, 5, 6, 7, 8, 9] and not district_visited[2]:
            district_visited[2] = True
        elif current[0] in [10, 11, 12, 13, 14] and not district_visited[3]:
            district_visited[3] = True

        if current == end:
            break

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_row < height and 0 <= next_col < width and matrix[next_row][next_col] != 'x' and not visited[next_row][next_col]:
                heapq.heappush(queue, (matrix[next_row][next_col], (next_row, next_col)))
                previous_node[next_row][next_col] = current

    path = []
    while end is not None:
        path.append(end)
        end = previous_node[end[0]][end[1]]
    path.reverse()

    return path if all(v for v in district_visited.values()) else None

matrix = [
    [18, 15, 'x', 'x', 1, 'x', 'x', 5, 8, 18, 18, 2, 'x', 11, 8],
    ['x', 17, 'x', 'x', 2, 'x', 16, 9, 7, 13, 16, 'x', 'x', 'x'],
    [10, 'x', 1, 14, 1, 10, 15, 4, 'x', 'x', 8, 11, 10, 'x', 'x'],
    [19, 'x', 'x', 9, 8, 18, 5, 2, 12, 'x', 13, 'x', 'x', 15, 11],
    [1, 14, 6, 6, 6, 'x', 'x', 'x', 13, 13, 'x', 'x', 'x', 'x'],
    [2, 3, 8, 5, 7, 'x', 'x', 'x', 19, 'x', 16, 'x', 'x', 'x', 'x'],
    ['x', 'x', 17, 18, 'x', 19, 'x', 'x', 7, 8, 17, 'x', 'x', 'x', 'x'],
    [4, 'x', 4, 14, 17, 6, 'x', 'x', 'x', 15, 6, 'x', 18, 10],
    [7, 'x', 3, 11, 10, 'x', 'x', 'x', 8, 'x', 'x', 10, 'x', 'x', 'x'],
    [4, 16, 2, 11, 'x', 'x', 'x', 14, 'x', 13, 'x', 'x', 'x', 'x', 'x'],
    [14, 20, 7, 14, 'x', 'x', 'x', 'x', 'x', 5, 'x', 10, 16, 'x'],
    [1, 14, 'x', 'x', 'x', 4, 14, 19, 'x', 18, 'x', 17, 15, 14],
    ['x', 'x', 15, 4, 5, 19, 18, 'x', 19, 11, 3, 12, 'x', 10],
    [1, 'x', 'x', 13, 'x', 16, 4, 'x', 'x', 8, 'x', 9, 'x'],
    ['x', 'x', 12, 11, 7, 'x', 8, 14, 3, 'x', 11, 'x', 14, 13, 'x']
]

start = (1, 11)
end = (7, 2)

path = dijkstra(matrix, start, end)
print(path)
