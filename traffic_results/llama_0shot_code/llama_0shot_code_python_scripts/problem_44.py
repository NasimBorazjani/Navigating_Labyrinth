
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # north, south, west, east
    visited = [[0 for _ in range(width)] for _ in range(height)]
    prev = [[None for _ in range(width)] for _ in range(height)]
    queue = [(matrix[start[0]][start[1]], start)]
    visited[start[0]][start[1]] = 1
    while queue:
        dist, current = heapq.heappop(queue)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = prev[current[0]][current[1]]
            return path[::-1]  # shortest path from start to end
        for direction in directions:
            next_node = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_node[0] < height and 0 <= next_node[1] < width and
                    matrix[next_node[0]][next_node[1]] != 'x' and
                    not visited[next_node[0]][next_node[1]]):
                visited[next_node[0]][next_node[1]] = 1
                heapq.heappush(queue, (dist + matrix[next_node[0]][next_node[1]], next_node))
                prev[next_node[0]][next_node[1]] = current
    return []  # if no path found

def solve(matrix):
    matrix = [list(row) for row in matrix]
    start = (8, 10)
    end = (3, 4)
    height = len(matrix)
    width = len(matrix[0])
    districts = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if matrix[i][j] != 'x':
                if i <= 2:
                    districts[i][j] = 1
                elif i <= 7:
                    districts[i][j] = 2
                else:
                    districts[i][j] = 3
    path = dijkstra(districts, start, end)
    if not path:
        return 'No path found'
    matrix_path = dijkstra(matrix, start, end)
    district_count = {1: 0, 2: 0, 3: 0}
    for node in matrix_path:
        district_count[districts[node[0]][node[1]]] += 1
    if district_count[1] == district_count[2] == district_count[3] == 1:
        return matrix_path
    else:
        return 'Not all districts are visited'

matrix = [
    ['x', 16, 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'],
    ['x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'],
    ['x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14],
    ['x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5],
    [2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19],
    [19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10],
    ['x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15],
    [2, 'x', 11, 'x', 12, 11, 'x', 15, 10, 6],
    [19, 'x', 16, 5, 'x', 'x', 'x', 11, 11, 8],
    [12, 'x', 2, 'x', 'x', 'x', 15, 'x', 'x']
]

print(solve(matrix))
