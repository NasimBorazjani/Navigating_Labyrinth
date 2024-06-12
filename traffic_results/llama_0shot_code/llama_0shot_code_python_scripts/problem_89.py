
import heapq

def dijkstra(matrix, start, end, districts):
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    visited = [[False for _ in range(n)] for _ in range(m)]
    distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    previous_nodes = [[None for _ in range(n)] for _ in range(m)]
    distances[start[0]][start[1]] = 0
    district_visited = [False for _ in range(len(districts))]

    queue = [(0, start)]
    while queue:
        current_distance, (i, j) = heapq.heappop(queue)
        if (i, j) == end:
            path = []
            while (i, j) is not None:
                path.append((i, j))
                i, j = previous_nodes[i][j]
            return path[::-1]
        if not visited[i][j]:
            visited[i][j] = True
            district = None
            for d, district_range in enumerate(districts):
                if district_range[0] <= i < district_range[1]:
                    district = d
                    break
            if district is not None and not district_visited[district]:
                district_visited[district] = True
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j] and matrix[new_i][new_j] != 'x':
                    distance = current_distance + matrix[new_i][new_j]
                    if distance < distances[new_i][new_j]:
                        distances[new_i][new_j] = distance
                        previous_nodes[new_i][new_j] = (i, j)
                        heapq.heappush(queue, (distance, (new_i, new_j)))
    return [] # if there is no path

matrix = [
    ['x', 'x', 'x', 7, 11, 16, 13, 19, 15, 'x', 19, 'x', 'x', 16],
    [9, 'x', 14, 'x', 7, 'x', 'x', 17, 9, 'x', 'x', 'x', 19],
    ['x', 11, 6, 18, 'x', 19, 4, 'x', 'x', 'x', 19, 12, 4, 17],
    [5, 12, 15, 3, 'x', 'x', 'x', 'x', 7, 'x', 11, 17, 20, 20],
    [6, 'x', 11, 15, 11, 17, 16, 5, 'x', 3, 4, 20, 'x', 14],
    ['x', 11, 'x', 6, 'x', 16, 5, 11, 'x', 14, 4, 7],
    ['x', 6, 'x', 17, 'x', 15, 7, 'x', 3, 16, 7, 15],
    [7, 'x', 'x', 8, 1, 'x', 'x', 14, 'x', 'x', 18, 'x', 19],
    [13, 'x', 'x', 'x', 2, 9, 19, 'x', 16, 11, 5, 'x', 11],
    ['x', 17, 15, 18, 'x', 7, 'x', 15, 13, 'x', 14, 2, 'x', 19],
    ['x', 'x', 'x', 14, 7, 19, 'x', 'x', 9, 9, 'x', 'x', 'x'],
    ['x', 3, 13, 15, 18, 17, 'x', 'x', 9, 4, 'x', 12, 10, 14],
    [15, 'x', 6, 19, 19, 19, 'x', 1, 8, 4, 17, 14, 'x', 'x'],
    [8, 'x', 14, 7, 12, 6, 8, 'x', 5, 'x', 11, 11, 'x', 'x']
]

start = (3, 13)
end = (4, 0)
districts = [(0, 4), (4, 6), (6, 14)]

path = dijkstra(matrix, start, end, districts)
print(path)
