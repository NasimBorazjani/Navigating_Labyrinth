
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    # Convert the matrix into a graph
    graph = {(i, j): {} for i in range(rows) for j in range(cols) if matrix[i][j] != 'x'}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'x':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                        graph[(i, j)][(ni, nj)] = matrix[ni][nj]

    # Apply Dijkstra's algorithm
    queue = [(matrix[start[0]][start[1]], start, [])]
    visited = set()
    while queue:
        time, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[::-1]  # Reverse the path to start from the start node
            for neighbor, edge_time in graph[node].items():
                heapq.heappush(queue, (time + edge_time, neighbor, path))

    return None  # No path found

# Test the function
matrix = [
    "2x14x196xx1418x",
    "x10115xxx172912",
    "1314x2xx1010xx",
    "91731544x915169",
    "1073871637xx11145x",
    "16201619183xx1114x",
    "x18xx41961415177x",
    "x2xxxxx719xx",
    "x3141xx1841210x",
    "2x1613xx177xx1910x",
    "x410xxx7x197xx"
]
matrix = [[int(c) if c.isdigit() else c for c in row] for row in matrix]
start, end = (6, 9), (3, 0)
path = shortest_path(matrix, start, end)
print(path)
