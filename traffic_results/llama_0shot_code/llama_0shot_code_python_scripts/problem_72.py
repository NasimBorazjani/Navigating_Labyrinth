
import heapq

def dijkstra(matrix, start, end):
    m, n = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    visited = [[False for _ in range(n)] for _ in range(m)]
    distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    previous_nodes = [[None for _ in range(n)] for _ in range(m)]
    distances[start[0]][start[1]] = 0
    districts_visited = [False, False, False]

    heap = [(0, start)]
    while heap:
        current_distance, (i, j) = heapq.heappop(heap)
        if (i, j) == end:
            path = []
            while (i, j) is not None:
                path.append((i, j))
                i, j = previous_nodes[i][j]
            return path[::-1]
        if distances[i][j] < current_distance:
            continue
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and matrix[ni][nj] != 'x':
                distance = current_distance + matrix[ni][nj]
                if distance < distances[ni][nj]:
                    distances[ni][nj] = distance
                    previous_nodes[ni][nj] = (i, j)
                    heapq.heappush(heap, (distance, (ni, nj)))
                if ni < 4:  # district 1
                    districts_visited[0] = True
                elif ni < 6:  # district 2
                    districts_visited[1] = True
                else:  # district 3
                    districts_visited[2] = True
                if all(districts_visited):
                    return distances, previous_nodes
    return distances, previous_nodes

matrix = [
    ['x', 'x', 'x', 'x', 9, 1, 14, 'x', 'x', 'x', 11, 15, 12],
    [2, 'x', 18, 'x', 14, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [10, 'x', 3, 'x', 'x', 'x', 10, 9, 7, 'x', 'x', 'x'],
    [1, 18, 2, 6, 'x', 'x', 1, 5, 'x', 'x', 6, 'x', 'x'],
    [4, 14, 12, 3, 2, 2, 15, 8, 19, 3, 18, 'x', 'x'],
    [5, 6, 2, 2, 13, 'x', 7, 3, 12, 'x', 16, 10, 5],
    ['x', 2, 13, 'x', 'x', 9, 5, 'x', 'x', 7, 10, 11],
    [17, 10, 3, 11, 4, 'x', 'x', 19, 'x', 5, 'x', 'x', 9],
    [13, 'x', 'x', 'x', 'x', 9, 13, 4, 7, 'x', 13, 10, 'x'],
    ['x', 'x', 'x', 9, 'x', 8, 8, 14, 'x', 'x', 19, 'x', 'x'],
    [6, 'x', 'x', 'x', 'x', 1, 11, 'x', 4, 13, 'x', 'x'],
    ['x', 'x', 'x', 11, 11, 'x', 9, 16, 12, 'x', 6, 'x', 5],
    [16, 19, 14, 'x', 5, 13, 'x', 'x', 'x', 'x', 'x', 13, 'x']
]

start, end = (6, 12), (5, 0)
distances, previous_nodes = dijkstra(matrix, start, end)
path = []
while end is not None:
    path.append(end)
    end = previous_nodes[end[0]][end[1]]
path.append(start)
path = path[::-1]
print(path)
