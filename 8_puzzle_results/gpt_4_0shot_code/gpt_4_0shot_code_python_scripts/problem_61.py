
import heapq

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] != '_':
                x, y = divmod(puzzle[i][j]-1, 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def solve(puzzle):
    start = [list(row) for row in puzzle]
    goal = [[93, 92, 83, 67, 60], [59, 54, 50, 21, 19], [14, 12, 9, 8, '_']]
    heap = [(manhattan_distance(start), start)]
    visited = set()
    moves = {str(start): []}

    while heap:
        (h, puzzle) = heapq.heappop(heap)
        if puzzle == goal:
            return moves[str(puzzle)]
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for i in range(3):
                for j in range(5):
                    if puzzle[i][j] == '_':
                        x, y = i + dx, j + dy
                        if 0 <= x < 3 and 0 <= y < 5:
                            puzzle[i][j], puzzle[x][y] = puzzle[x][y], puzzle[i][j]
                            if str(puzzle) not in visited:
                                visited.add(str(puzzle))
                                heapq.heappush(heap, (h - manhattan_distance(puzzle) + manhattan_distance(puzzle), puzzle))
                                moves[str(puzzle)] = moves[str(puzzle)] + [puzzle[x][y]]
                            puzzle[i][j], puzzle[x][y] = puzzle[x][y], puzzle[i][j]

puzzle = [[93, 83, 50, 21, 67], [59, '_', 60, 19, 8], [14, 12, 92, 54, 9]]
print(solve(puzzle))
