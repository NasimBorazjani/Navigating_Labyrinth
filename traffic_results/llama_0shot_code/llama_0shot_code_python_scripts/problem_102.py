
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    previous_node = [[None for _ in range(cols)] for _ in range(rows)]
    queue = [(matrix[start[0]][start[1]], start)]
    district_visited = [0, 0, 0]

    while queue:
        dist, current = heapq.heappop(queue)
        if visited[current[0]][current[1]] == 1:
            continue
        visited[current[0]][current[1]] = 1
        if current[0] in [0, 1, 2, 3, 4, 5]:
            district_visited[0] = 1
        elif current[0] in [6, 7, 8, 9, 10, 11, 12]:
            district_visited[1] = 1
        elif current[0] in [13, 14, 15, 16, 17, 18, 19]:
            district_visited[2] = 1
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = previous_node[current[0]][current[1]]
            return path[::-1], district_visited
        for direction in directions:
            next_node = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_node[0] < rows and 0 <= next_node[1] < cols and
                    matrix[next_node[0]][next_node[1]] != 'x' and
                    visited[next_node[0]][next_node[1]] == 0):
                heapq.heappush(queue, (matrix[next_node[0]][next_node[1]], next_node))
                previous_node[next_node[0]][next_node[1]] = current
    return None

matrix = [
    ['x', 13, 'x', 'x', 'x', 'x', 3, 4, 'x', 'x', 9, 'x', 18, 7, 2],
    [1, 10, 17, 'x', 'x', 'x', 11, 13, 'x', 10, 'x', 9, 13, 'x', 'x'],
    ['x', 'x', 7, 18, 'x', 'x', 'x', 'x', 7, 'x', 'x', 'x', 1, 16],
    [10, 'x', 'x', 'x', 13, 'x', 2, 9, 'x', 'x', 8, 'x', 'x', 5, 'x'],
    ['x', 7, 12, 'x', 1, 18, 14, 'x', 'x', 'x', 16, 'x', 'x', 19],
    [5, 1, 13, 17, 11, 14, 16, 'x', 14, 'x', 18, 5, 'x', 18, 'x'],
    ['x', 15, 19, 4, 'x', 13, 'x', 'x', 18, 'x', 17, 'x', 'x', 'x'],
    [3, 7, 'x', 'x', 'x', 12, 'x', 17, 4, 13, 19, 3, 10],
    [11, 'x', 'x', 'x', 'x', 2, 2, 19, 13, 4, 7, 17, 16, 'x', 17],
    [12, 5, 4, 'x', 'x', 'x', 'x', 12, 8, 11, 'x', 17, 14, 19, 2],
    [4, 10, 'x', 'x', 6, 11, 16, 17, 'x', 'x', 18, 'x', 17, 'x', 'x'],
    ['x', 'x', 'x', 'x', 11, 9, 18, 17, 12, 'x', 'x', 'x', 'x', 'x', 1],
    [18, 13, 7, 'x', 'x', 5, 4, 13, 'x', 'x', 19, 12, 1, 18, 'x'],
    [15, 'x', 17, 'x', 'x', 'x', 17, 'x', 'x', 10, 'x', 15, 16, 'x']
]

start = (5, 0)
end = (7, 13)

path, district_visited = dijkstra(matrix, start, end)

if path is not None:
    print("Path:", [(i, j) for i, j in path])
    print("Districts visited:", district_visited)
else:
    print("No path found")
