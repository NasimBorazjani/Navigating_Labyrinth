
import heapq

def heuristic(puzzle):
    goal = [[82, 71, 69, 62], [55, 54, 53, 39], [35, 16, 11, '_']]
    return sum(p != g for row_p, row_g in zip(puzzle, goal) for p, g in zip(row_p, row_g))

def get_moves(puzzle):
    for i, row in enumerate(puzzle):
        for j, p in enumerate(row):
            if p == '_':
                for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= i + x < len(puzzle) and 0 <= j + y < len(row):
                        new_puzzle = [r.copy() for r in puzzle]
                        new_puzzle[i][j], new_puzzle[i + x][j + y] = new_puzzle[i + x][j + y], new_puzzle[i][j]
                        yield new_puzzle

def solve(puzzle):
    goal = [[82, 71, 69, 62], [55, 54, 53, 39], [35, 16, 11, '_']]
    queue = [(heuristic(puzzle), puzzle)]
    seen = {str(puzzle)}
    while queue:
        _, puzzle = heapq.heappop(queue)
        if puzzle == goal:
            return puzzle
        for move in get_moves(puzzle):
            if str(move) not in seen:
                heapq.heappush(queue, (heuristic(move), move))
                seen.add(str(move))

initial_state = [[82, '_', 39, 54], [55, 62, 53, 35], [69, 16, 11, 71]]
print(solve(initial_state))
