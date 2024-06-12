
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(pos):
    x, y = pos
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:
            result.append((nx, ny))
    return result

def solve(puzzle):
    start = None
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '_':
                start = (i, j)

    queue = PriorityQueue()
    queue.put((0, start, puzzle, []))
    visited = set()

    while not queue.empty():
        _, pos, puzzle, path = queue.get()
        visited.add(tuple(tuple(row) for row in puzzle))

        if puzzle == [[99, 97, 50], [92, 49, 46], [91, 25, '_']]:
            return path

        for neighbor in get_neighbors(pos):
            x, y = pos
            nx, ny = neighbor
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
            if tuple(tuple(row) for row in new_puzzle) not in visited:
                new_path = path + [new_puzzle[nx][ny]]
                queue.put((len(new_path) + heuristic(neighbor, (2, 2)), neighbor, new_puzzle, new_path))

print(solve([[46, 50, 97], [92, 49, 99], [91, 25, '_']]))
