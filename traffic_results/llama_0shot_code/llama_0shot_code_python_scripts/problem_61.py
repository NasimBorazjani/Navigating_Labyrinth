
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def get_district(i, j):
        if i <= 1: return 1
        if i <= 5: return 2
        return 3

    def valid(i, j):
        return 0 <= i < rows and 0 <= j < cols and matrix[i][j] != 'x'

    def get_neighbors(i, j):
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if valid(ni, nj):
                yield ni, nj

    visited = [[False]*cols for _ in range(rows)]
    district_visited = [False]*3
    heap = [(matrix[start[0]][start[1]], start)]
    path = {start: None}

    while heap:
        cost, (i, j) = heapq.heappop(heap)
        if (i, j) == end:
            break
        if not visited[i][j]:
            visited[i][j] = True
            district_visited[get_district(i, j) - 1] = True
            if not all(district_visited):  # Not all districts visited
                for ni, nj in get_neighbors(i, j):
                    if not visited[ni][nj] and get_district(ni, nj) != get_district(i, j):
                        heapq.heappush(heap, (matrix[ni][nj], (ni, nj)))
                        path[(ni, nj)] = (i, j)
            else:  # All districts visited, find the shortest path to the end
                for ni, nj in get_neighbors(i, j):
                    if not visited[ni][nj]:
                        heapq.heappush(heap, (matrix[ni][nj], (ni, nj)))
                        path[(ni, nj)] = (i, j)

    # Reconstruct the path from end to start
    node = end
    while node is not None:
        node = path[node]

    # Return the path from start to end
    node = end
    path = []
    while node is not None:
        path.append(node)
        node = path[node]
    return path[::-1]

matrix = [
    [13, 13, 16, 8, 'x', 19, 1, 18, 13, 8, 'x', 7, 'x'],
    ['x', 13, 'x', 15, 'x', 12, 20, 1, 13, 19, 4, 17, 'x'],
    ['x', 12, 9, 11, 13, 12, 2, 12, 19, 5, 19, 16, 8],
    ['x', 12, 18, 19, 'x', 7, 'x', 12, 3, 2, 'x', 16, 11],
    ['x', 7, 'x', 'x', 8, 13, 15, 3, 1, 'x', 15, 15, 'x'],
    [11, 9, 'x', 16, 2, 10, 1, 2, 16, 1, 'x', 10, 12],
    ['x', 'x', 9, 9, 7, 'x', 6, 'x', 'x', 10, 7, 2, 'x'],
    ['x', 13, 10, 8, 1, 11, 'x', 'x', 'x', 'x', 'x', 'x'],
    [11, 14, 'x', 'x', 'x', 'x', 4, 8, 'x', 'x', 18, 'x'],
    [13, 14, 'x', 10, 'x', 'x', 16, 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 16, 10, 'x', 17, 12, 'x', 10, 'x', 5],
    [9, 'x', 10, 19, 16, 'x', 14, 16, 12, 15, 7, 'x'],
    [1, 8, 10, 14, 'x', 6, 9, 'x', 'x', 8, 11, 11]
]

print(dijkstra(matrix, (3, 12), (6, 2)))
