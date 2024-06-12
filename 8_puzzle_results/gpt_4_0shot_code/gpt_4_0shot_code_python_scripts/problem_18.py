
def solve_puzzle(puzzle):
    goal = [[98, 96, 88], [85, 83, 80], [52, 50, '_']]
    moves = []
    while puzzle != goal:
        empty = [(index, row.index('_')) for index, row in enumerate(puzzle) if '_' in row][0]
        if empty[0] < 2:
            puzzle[empty[0]][empty[1]], puzzle[empty[0] + 1][empty[1]] = puzzle[empty[0] + 1][empty[1]], puzzle[empty[0]][empty[1]]
            moves.append(puzzle[empty[0]][empty[1]])
        elif empty[1] < 2:
            puzzle[empty[0]][empty[1]], puzzle[empty[0]][empty[1] + 1] = puzzle[empty[0]][empty[1] + 1], puzzle[empty[0]][empty[1]]
            moves.append(puzzle[empty[0]][empty[1]])
    return moves

puzzle = [[88, 52, 85], [98, 96, 83], [50, 80, '_']]
print(solve_puzzle(puzzle))
