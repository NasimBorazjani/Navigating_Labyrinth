
def solve_puzzle(initial_state):
    goal_state = [[85, 76, 66], [45, 41, 21], [13, '_', '_']]
    moves = []
    while initial_state != goal_state:
        empty_spot = [(index, row.index('_')) for index, row in enumerate(initial_state) if '_' in row][0]
        if empty_spot[0] > 0:
            initial_state[empty_spot[0]][empty_spot[1]], initial_state[empty_spot[0] - 1][empty_spot[1]] = initial_state[empty_spot[0] - 1][empty_spot[1]], initial_state[empty_spot[0]][empty_spot[1]]
            moves.append(initial_state[empty_spot[0]][empty_spot[1]])
        elif empty_spot[1] > 0:
            initial_state[empty_spot[0]][empty_spot[1]], initial_state[empty_spot[0]][empty_spot[1] - 1] = initial_state[empty_spot[0]][empty_spot[1] - 1], initial_state[empty_spot[0]][empty_spot[1]]
            moves.append(initial_state[empty_spot[0]][empty_spot[1]])
    return moves

initial_state = [[45, 13, '_'], [66, 41, 76], [85, 21, 74]]
print(solve_puzzle(initial_state))
