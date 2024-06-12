
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (3, 12), (7, 3)
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 'x':
                        graph[(i, j)].append(((x, y), matrix[i][j]))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(unvisited, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()

    return path

matrix = [
    "10x x x16 9x 13 12 8x 16 17",
    "9 2x x x5 x x x12 x 3x x",
    "x x7 3 12x 11 18 10x x13x",
    "x6x 19 2x x11 13 13 1x 7",
    "x x11x 16 16 4 12 5 20 2 4 15",
    "19x 18 5 11x x 3 17 18 3 8 18",
    "12x 9x x x x x9 4 15 16x 9",
    "x15x 6 10x 1 1x 9 4 7 1x",
    "x19 15x 1 10 5 17x 8x 1x",
    "x x x x5x 1x x x7 4x x",
    "9x 4x 5 13x 15x x x18 9 15",
    "17 2x x x18 8x 8x 15 19x x"
]

matrix = [list(row.replace(' ', '')) for row in matrix]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'x':
            matrix[i][j] = 'x'
        else:
            matrix[i][j] = int(matrix[i][j])

print(shortest_path(matrix))
