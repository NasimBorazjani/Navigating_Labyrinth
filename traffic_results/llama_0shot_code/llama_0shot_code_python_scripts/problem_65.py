
import heapq

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = (8, 11), (2, 3)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    districts = [
        [(0, 1), (0, 2)],
        [(0, 3), (0, 7)],
        [(0, 8), (0, 12)]
    ]
    for district in districts:
        if not any(node[0] in range(district[0][0], district[1][0]+1) and node[1] in range(district[0][1], district[1][1]+1) for node in path):
            shortest_node = min(((i, j), matrix[i][j]) for i in range(rows) for j in range(cols) if matrix[i][j] != 'x' and i in range(district[0][0], district[1][0]+1) and j in range(district[0][1], district[1][1]+1)), key=lambda x: x[1])[0]
            path.insert(next(i for i, node in enumerate(path) if node[0] > shortest_node[0])+1, shortest_node)

    return path

matrix = [
    "11 x x x 15 5 18 4 1 17 14 x 9",
    "x 10 10 7 12 12 6 x x 8 4 19 11",
    "17 x x 12 8 x x x 14 19 x 18 16",
    "17 x 16 x x 17 4 x 15 x x x 17",
    "17 x x 6 x x 12 6 10 3 11 x 19",
    "10 x 9 15 17 4 x x x x 14 17 18",
    "4 x x x x 13 18 13 x 17 12 x 19",
    "x 2 11 7 6 14 9 x 12 17 9 13 14",
    "x 18 16 x x x 11 6 12 x x 10 x",
    "5 3 x x x 5 x 14 x x x x x",
    "18 x x x x 14 x x 13 1 3 x x",
    "1 16 10 x x 14 13 x 10 x 1 x 18",
    "8 x x 10 2 10 x x x x x 13 5"
]
matrix = [[int(cell) if cell.isdigit() else 'x' for cell in row] for row in matrix]

print(shortest_path(matrix))
