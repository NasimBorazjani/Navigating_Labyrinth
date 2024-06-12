
import heapq
import copy

def heuristic(puzzle):
    h = 0
    goal = [[97, 76, 72, 65, 61], [53, 52, 49, 26, 22], [13, 12, '_', 89, 64]]
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] != goal[i][j] and puzzle[i][j] != '_':
                h += 1
    return h

def get_moves(puzzle):
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] == '_':
                x, y = i, j
    moves = []
    if x > 0:
        moves.append((x - 1, y))
    if x < 2:
        moves.append((x + 1, y))
    if y > 0:
        moves.append((x, y - 1))
    if y < 4:
        moves.append((x, y + 1))
    return x, y, moves

def solve(puzzle):
    start = puzzle
    heap = [(heuristic(start), start)]
    visited = set()
    while heap:
        (h, puzzle) = heapq.heappop(heap)
        if puzzle in visited:
            continue
        visited.add(puzzle)
        if h == 0:
            return puzzle
        x, y, moves = get_moves(puzzle)
        for move in moves:
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[x][y], new_puzzle[move[0]][move[1]] = new_puzzle[move[0]][move[1]], new_puzzle[x][y]
            heapq.heappush(heap, (heuristic(new_puzzle), new_puzzle))

puzzle = [[12, 76, '_', 72, 53], [61, 97, 49, 65, 52], [89, 64, 22, 26, 13]]
print(solve(puzzle))
