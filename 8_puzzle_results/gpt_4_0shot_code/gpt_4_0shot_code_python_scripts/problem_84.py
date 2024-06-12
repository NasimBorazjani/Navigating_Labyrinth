
import heapq
import copy

def heuristic(puzzle):
    goal = [[96, 85, 80, 76, 72], [89, 60, 55, 42, 29], [27, 12, '_', '_', '_']]
    return sum(tile != goal_tile for row, goal_row in zip(puzzle, goal) for tile, goal_tile in zip(row, goal_row))

def get_moves(puzzle):
    for i, row in enumerate(puzzle):
        for j, tile in enumerate(row):
            if tile == '_':
                for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= i + x < len(puzzle) and 0 <= j + y < len(row):
                        new_puzzle = copy.deepcopy(puzzle)
                        new_puzzle[i][j], new_puzzle[i + x][j + y] = new_puzzle[i + x][j + y], new_puzzle[i][j]
                        yield new_puzzle

def solve(puzzle):
    goal = [[96, 85, 80, 76, 72], [89, 60, 55, 42, 29], [27, 12, '_', '_', '_']]
    queue = [(heuristic(puzzle), puzzle)]
    seen = {str(puzzle)}
    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            return current
        for move in get_moves(current):
            if str(move) not in seen:
                heapq.heappush(queue, (heuristic(move), move))
                seen.add(str(move))
    return None

initial = [[85, 96, 29, 80, 12], [60, '_', 76, 42, 82], [27, 89, 72, 37, 55]]
print(solve(initial))
