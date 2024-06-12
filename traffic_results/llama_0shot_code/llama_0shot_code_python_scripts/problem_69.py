
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def get_neighbors(node):
        i, j = node
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != 'x':
                yield (ni, nj), matrix[ni][nj]

    def heuristic(node):
        i, j = node
        di, dj = abs(i - end[0]), abs(j - end[1])
        return di + dj

    queue = [(0, start, [])]  # (cost, node, path)
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path[1:]  # exclude start node
            for neighbor, weight in get_neighbors(node):
                if len(set(i for i, _ in path)) < 3 or neighbor in {(0, 1), (6, 3)}:
                    heapq.heappush(queue, (cost + weight + heuristic(neighbor), neighbor, path))
    return None

matrix = [
    [17, 'x', 'x', 'x', 5, 'x', 'x', 12, 16, 'x', 'x', 5, 16],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 4, 6],
    [9, 'x', 'x', 'x', 'x', 19, 'x', 'x', 13, 6, 11, 19],
    [1, 'x', 'x', 'x', 13, 'x', 'x', 3, 2, 7, 4, 3],
    ['x', 'x', 'x', 14, 19, 20, 10, 13, 14, 'x', 9, 3],
    [15, 'x', 11, 7, 'x', 11, 6, 16, 'x', 'x', 'x', 8, 19],
    [19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, 'x', 5],
    ['x', 3, 17, 'x', 'x', 6, 17, 19, 'x', 'x', 14, 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 14, 10, 14, 13, 'x', 13, 'x', 'x'],
    [15, 5, 4, 'x', 'x', 'x', 'x', 2, 12, 6, 'x', 16, 14],
    [10, 'x', 'x', 'x', 9, 'x', 'x', 'x', 'x', 13, 2, 'x'],
    ['x', 'x', 17, 'x', 'x', 'x', 7, 'x', 16, 'x', 'x'],
    [12, 10, 'x', 15, 16, 'x', 7, 11, 7, 'x', 17, 'x']
]

start, end = (1, 12), (6, 3)
path = shortest_path(matrix, start, end)
print(path)
