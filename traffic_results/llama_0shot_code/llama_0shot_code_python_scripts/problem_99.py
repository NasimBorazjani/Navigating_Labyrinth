
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    graph = {(i, j): [] for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    districts = {(i, j): (i // 5) + 1 for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 'x':
                        graph[(i, j)].append((matrix[i][j], (x, y)))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for time, neighbor in graph[current_node]:
            distance = current_distance + time
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [current_node]
                if districts[neighbor] != districts[end] or neighbor == end:
                    heapq.heappush(queue, (distance, neighbor))
    return paths[end] + [end]

matrix = [
    "7 6 11 x x x 19 x 9 15 12 8 10 15 5",
    "9 14 x x x x x x x x 18 2 11 x 10",
    "14 5 x x 4 4 12 x 18 x 17 11 3 18 19",
    "18 17 x 8 x x 9 x x 8 19 10 x x x",
    "7 x x 11 4 x x 10 1 2 3 12 8 12 15",
    "x 3 7 8 x x x x 4 16 13 19 14 10 13",
    "18 1 2 x 16 20 5 x 2 4 20 12 14 18 16",
    "1 x 1 x 15 19 11 9 19 16 x x x x 19",
    "x 8 x 1 7 x 2 3 x x x x 1 3 x",
    "6 16 x 3 x 18 x 2 18 x x 16 x x 8",
    "x 9 x 5 2 x x x x 17 x 6 18 14 x",
    "x x x x x x x 18 x x 3 x 10 x x",
    "x 2 15 x 5 15 18 8 19 x x x x x 10",
    "x x 4 x 7 2 2 x 19 x x x x x x",
    "17 x x x 5 x x x 4 1 18 x 9 2 8"
]
matrix = [list(map(lambda x: int(x) if x != 'x' else 'x', row.split())) for row in matrix]

start, end = (4, 14), (8, 3)
result = shortest_path(matrix, start, end)
print(result)
