
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    moves = {(0, 1): 'down-right', (0, -1): 'up-right', (1, 0): 'down-left', (-1, 0): 'up-left'}
    target = ['zeta', 'sumac', 'showy', 'smeek', 'ajava']
    while queue:
        current_board, direction = queue.popleft()
        current_state = tuple(tuple(row) for row in current_board)
        if current_state in visited:
            continue
        visited.add(current_state)
        blank_row, blank_col = current_board.index('_'), current_board[0].index('_')
        for dr, dc in moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < len(current_board) and 0 <= new_col < len(current_board[0]) and current_board[new_row][new_col] == '_':
                continue
            new_board = [list(row) for row in current_board]
            new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
            new_state = ''.join(''.join(row) for row in new_board)
            if new_state == ''.join(target):
                return [moves[(dr, dc)]] if direction is None else [moves[(dr, dc)]] + direction
            queue.append((new_board, [moves[(dr, dc)]] if direction is None else [moves[(dr, dc)]] + direction))
    return []

initial_board = [['u', 'z', 's', 't', 'a'], ['s', 'e', 'm', 'o', 'c'], ['a', 'h', '_', 'w', 'y'], ['s', 'a', 'e', 'm', 'k'], ['a', 'j', 'e', 'v', 'a']]

print(bfs(initial_board, ['zeta', 'sumac', 'showy', 'smeek', 'ajava']))
