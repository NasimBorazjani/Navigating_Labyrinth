
import heapq

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(0, start)]  # (cost, position)
    visited = set()
    while queue:
        (cost, (r, c)) = heapq.heappop(queue)
        if (r, c) not in visited:
            visited.add((r, c))
            if (r, c) == end:
                return cost
            for nr, nc in get_neighbors(r, c):
                heapq.heappush(queue, (cost + matrix[nr][nc] + heuristic((nr, nc), end), (nr, nc)))
    return float('inf')

def get_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    path = [end]
    current = end
    while current != start:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                path.append((nr, nc))
                current = (nr, nc)
                break
    path.append(start)
    return path[::-1]

def solve(matrix, start, end):
    district_rows = [range(0, 4), range(4, 5), range(5, 10)]
    districts = {r: i+1 for i, rows in enumerate(district_rows) for r in rows}
    penalty = 1000
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 'x':
                district_penalty = penalty if districts[r] != districts[start[0]] else 0
                matrix[r][c] += district_penalty
    shortest_path_cost = dijkstra(matrix, start, end)
    path = get_path(matrix, start, end)
    return [(i//cols, i%cols) for i in path]

matrix = [
    [7, 'x', 19, 11, 6, 'x', 4, 15, 9, 3],
    ['x', 'x', 13, 'x', 8, 17, 'x', 'x', 12, 16],
    ['x', 'x', 2, 'x', 15, 8, 'x', 13, 4, 'x'],
    [13, 11, 3, 3, 3, 'x', 'x', 'x', 'x', 'x'],
    [1, 16, 14, 6, 14, 17, 4, 9, 1, 'x'],
    ['x', 4, 9, 'x', 17, 17, 'x', 13, 2, 9],
    ['x', 'x', 'x', 'x', 5, 14, 17, 12, 7, 14],
    ['x', 15, 1, 'x', 'x', 'x', 'x', 'x', 13, 8],
    ['x', 'x', 19, 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 6, 9, 12, 8, 8, 'x', 18, 'x', 'x']
]

start = (5, 9)
end = (3, 1)

print(solve(matrix, start, end))
