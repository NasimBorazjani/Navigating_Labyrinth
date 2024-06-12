
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    district_ends = [(3,10), (4,4), (5,0)]
    district_visited = {0: False, 1: False, 2: False}
    path = []

    def get_neighbors(pos):
        row, col = pos
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < height and 0 <= new_col < width and matrix[new_row][new_col] != 'x':
                yield (new_row, new_col), matrix[new_row][new_col]

    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    while queue:
        dist, pos = heapq.heappop(queue)
        if pos not in visited:
            visited.add(pos)
            path.append(pos)
            if pos == end:
                return path
            for neighbor, _ in get_neighbors(pos):
                if neighbor not in visited:
                    heapq.heappush(queue, (matrix[neighbor[0]][neighbor[1]], neighbor))
            district = None
            for i in range(3):
                if pos[0] <= district_ends[i][0] and pos[1] <= district_ends[i][1]:
                    district = i
                    break
            if district is not None and not district_visited[district]:
                district_visited[district] = True
                for neighbor, _ in get_neighbors(pos):
                    if neighbor in district_ends and neighbor not in visited:
                        heapq.heappush(queue, (matrix[neighbor[0]][neighbor[1]], neighbor))
    return path

matrix = [
    [19, 7, 11, 'x', 3, 18, 8, 'x', 'x', 'x', 'x'],
    [12, 18, 6, 1, 13, 12, 14, 11, 13, 5, 19],
    [11, 10, 10, 18, 15, 'x', 12, 'x', 4, 17, 10],
    [4, 3, 3, 7, 'x', 19, 'x', 'x', 'x', 12, 9],
    ['x', 'x', 6, 19, 'x', 4, 14, 'x', 9, 4, 15],
    [4, 7, 6, 5, 8, 'x', 15, 3, 'x', 16, 3],
    [13, 'x', 'x', 1, 9, 1, 9, 'x', 'x', 'x', 'x'],
    [2, 13, 5, 9, 5, 'x', 6, 'x', 18, 'x', 3],
    [19, 'x', 2, 9, 4, 13, 'x', 'x', 'x', 16, 6],
    ['x', 'x', 'x', 12, 'x', 7, 9, 3, 9, 8, 1],
    ['x', 10, 'x', 12, 3, 6, 'x', 4, 12, 4, 'x']
]

start = (5, 10)
end = (3, 0)

path = dijkstra(matrix, start, end)
print(path)
