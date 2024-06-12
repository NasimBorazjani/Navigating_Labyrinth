
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # north, south, east, west

    # Convert matrix to graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start)]
    visited = set()
    path = {start: None}

    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                break
            for neighbor, edge_dist in graph[node].items():
                old_dist = path.get(neighbor, None)
                new_dist = dist + edge_dist
                if old_dist is None or new_dist < old_dist:
                    path[neighbor] = node
                    heapq.heappush(queue, (new_dist, neighbor))

    # Get the path from start to end
    node = end
    while node is not None:
        node = path[node]

    return node

# Test the function
matrix = [
    "x 10 17 x 4 8 x 7 x 12 19 4",
    "17 x 8 11 7 x x 19 x 11 x 13 18",
    "15 6 2 12 16 7 x 14 x 2 x 14 4",
    "x 18 4 x x x 13 14 2 4 20 10 7",
    "7 2 19 16 x x x 18 x x x 2 2",
    "10 17 14 7 17 3 3 19 x 19 x x 9",
    "9 x x x 5 18 13 6 x x x 19 10",
    "x x x x x 2 7 4 x x x x x",
    "x x 6 3 x 1 x x 14 x 18 x 1",
    "14 x 4 18 14 12 x x x x 2 x 13",
    "12 x 3 1 12 9 x 6 x x 16 x 18",
    "13 x 11 5 3 4 x x x x x x 18",
    "15 9 9 1 x 6 x x 14 x x 1 14"
]

matrix = [[int(x) if x.isdigit() else x for x in row] for row in matrix]

start, end = (5, 1), (2, 11)
path = dijkstra(matrix, start, end)
print(path)
