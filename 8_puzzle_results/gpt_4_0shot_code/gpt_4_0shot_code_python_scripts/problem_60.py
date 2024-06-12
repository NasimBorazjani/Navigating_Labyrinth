
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(pos):
    x, y = pos
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < 3 and ny >= 0 and ny < 4:
            result.append((nx, ny))
    return result

def solve(puzzle):
    start = None
    for i in range(3):
        for j in range(4):
            if puzzle[i][j] == '_':
                start = (i, j)

    queue = PriorityQueue()
    queue.put((0, start, []))
    seen = set()
    while not queue.empty():
        _, pos, path = queue.get()
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        if puzzle[x][y] == 31:
            return path
        for neighbor in get_neighbors(pos):
            nx, ny = neighbor
            if (nx, ny) not in seen:
                priority = heuristic(neighbor, (0, 0))
                queue.put((priority, neighbor, path + [puzzle[nx][ny]]))

puzzle = [[31, 92, 67, 69], [87, 35, 42, 72], [53, '_', 28, 19]]
print(solve(puzzle))
