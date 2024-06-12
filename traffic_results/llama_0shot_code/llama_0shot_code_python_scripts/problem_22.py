
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north, east, south, west

    # Create a graph from the matrix
    graph = [[(rows*cols+1, []) for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 'x':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                        graph[r][c] = (matrix[r][c], [(nr, nc)])

    # Use a priority queue to store the nodes to be visited
    queue = [(matrix[start[0]][start[1]], start)]
    distances = {start: (0, [])}

    while queue:
        d, (r, c) = heapq.heappop(queue)
        if (r, c) == end:
            return distances[(r, c)][1] + [end]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_d = d + graph[nr][nc][0]
                if (nr, nc) not in distances or new_d < distances[(nr, nc)][0]:
                    distances[(nr, nc)] = (new_d, distances[(r, c)][1] + [(r, c)])
                    heapq.heappush(queue, (new_d, (nr, nc)))

    return None

matrix = [
    [2, 2, 3, 'x', 2, 10, 'x', 8, 6, 'x'],
    [6, 11, 'x', 'x', 'x', 'x', 'x', 16, 'x', 7],
    [17, 17, 7, 12, 13, 15, 5, 6, 10, 13],
    [1, 15, 13, 3, 'x', 'x', 'x', 14, 'x', 9],
    [14, 'x', 'x', 6, 15, 2, 12, 18, 'x', 18],
    [11, 19, 1, 19, 10, 8, 'x', 14, 'x', 'x'],
    [11, 'x', 'x', 'x', 3, 'x', 'x', 7, 'x', 2],
    [16, 12, 'x', 'x', 'x', 5, 'x', 'x', 10, 'x'],
    ['x', 11, 'x', 2, 12, 'x', 8, 'x', 'x', 'x'],
    ['x', 'x', 16, 'x', 'x', 'x', 16, 16, 12, 'x']
]

print(shortest_path(matrix, (1, 0), (5, 7)))
