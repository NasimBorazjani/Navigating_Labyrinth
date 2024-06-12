
import heapq

def dijkstra(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up
    visited = [[0 for _ in range(width)] for _ in range(height)]
    distances = [[float('inf') for _ in range(width)] for _ in range(height)]
    previous_nodes = [[None for _ in range(width)] for _ in range(height)]
    districts = [[0 for _ in range(width)] for _ in range(height)]
    district_count = [0, 0, 0]

    for i in range(0, height, 3):
        for j in range(width):
            districts[i][j] = 1
            if i+1 < height:
                districts[i+1][j] = 1
                if i+2 < height:
                    districts[i+2][j] = 1

    for i in range(0, height, 3):
        for j in range(width):
            if matrix[i][j] == 'x':
                districts[i][j] = -1
                if i+1 < height:
                    districts[i+1][j] = -1
                    if i+2 < height:
                        districts[i+2][j] = -1

    distances[start[0]][start[1]] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if visited[current_node[0]][current_node[1]]:
            continue
        visited[current_node[0]][current_node[1]] = 1
        district_count[districts[current_node[0]][current_node[1]]-1] += 1
        if district_count[0] > 0 and district_count[1] > 0 and district_count[2] > 0:
            break
        for direction in directions:
            next_node = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= next_node[0] < height and 0 <= next_node[1] < width and matrix[next_node[0]][next_node[1]] != 'x' and not visited[next_node[0]][next_node[1]]:
                distance = current_distance + matrix[next_node[0]][next_node[1]]
                if distance < distances[next_node[0]][next_node[1]]:
                    distances[next_node[0]][next_node[1]] = distance
                    previous_nodes[next_node[0]][next_node[1]] = current_node
                    heapq.heappush(heap, (distance, next_node))

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node[0]][current_node[1]]
    path.reverse()

    return path

matrix = [
    [17, 9, 11, 5, 19, 4, 18, 'x', 5, 8, 'x', 'x'],
    [6, 13, 'x', 9, 2, 20, 11, 20, 7, 'x', 'x', 3],
    [4, 17, 'x', 18, 2, 10, 'x', 'x', 18, 'x', 'x', 'x'],
    [12, 10, 9, 14, 'x', 'x', 12, 6, 1, 2, 'x', 'x'],
    [5, 'x', 'x', 3, 'x', 4, 9, 14, 8, 'x', 10, 12],
    [1, 'x', 6, 3, 18, 18, 17, 10, 'x', 'x', 10],
    [13, 'x', 'x', 'x', 'x', 'x', 14, 1, 19, 'x', 7],
    [11, 'x', 'x', 5, 9, 'x', 18, 19, 13, 13, 'x', 10],
    ['x', 'x', 11, 'x', 'x', 'x', 'x', 14, 17, 'x', 13],
    [19, 'x', 'x', 'x', 'x', 19, 12, 7, 3, 14, 'x', 9],
    ['x', 12, 7, 15, 1, 16, 11, 9, 17, 'x', 'x']
]

start = (7, 0)
end = (3, 8)

path = dijkstra(matrix, start, end)
print(path)
