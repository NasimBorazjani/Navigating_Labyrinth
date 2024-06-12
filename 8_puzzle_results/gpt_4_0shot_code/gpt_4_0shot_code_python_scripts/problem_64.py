
from heapq import heappop, heappush

def get_location(rows, number):
    for i, row in enumerate(rows):
        for j, num in enumerate(row):
            if num == number:
                return i, j

def heuristic(puzzle, item_total_calc, total_calc):
    t = 0
    for row in range(3):
        for col in range(5):
            val = puzzle[row][col] - 1
            target_col = val % 5
            target_row = val // 5
            if target_row < 3 and target_col < 5:
                t += abs(target_row - row) + abs(target_col - col)
    return t

def solve(puzzle):
    start = puzzle
    prepend = []
    goal = [[100, 91, 80, 74, 56], [54, 44, 38, 36, 29], [19, 14, 13, 10, '_']]
    queue = [(heuristic(start, goal), start)]
    while queue:
        (h, state) = heappop(queue)
        if state == goal:
            return prepend
        moves = ['up', 'down', 'left', 'right']
        for move in moves:
            new_board = execute_move(state, move)
            if new_board:
                heappush(queue, (heuristic(new_board, goal), new_board))
                prepend.append(new_board)
    return []

def execute_move(state, direction):
    new_state = [row[:] for row in state]
    row, col = get_location(new_state, '_')
    if direction == 'up' and row > 0:
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
    elif direction == 'down' and row < 2:
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
    elif direction == 'left' and col > 0:
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
    elif direction == 'right' and col < 4:
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
    else:
        return None
    return new_state

puzzle = [[54, 100, 91, 80, 56], [19, '_', 38, 74, 29], [14, 36, 44, 13, 10]]
print(solve(puzzle))
