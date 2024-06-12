
from collections import deque

def bfs(init_board):
    target_words = ['saiph', 'lierre', 'accend', 'evenly']
    queue = deque([(init_board, '')])
    visited = set()
    
    while queue:
        board, path = queue.popleft()
        if board[2][0] == '_' and board[2][1:] == list(target_words[0]) and board[3] == list(target_words[1]) and board[0] == list(target_words[2]) and board[1] == list(target_words[3]):
            return path
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_board, new_path = swap(board, direction)
            if new_board not in visited:
                visited.add(new_board)
                queue.append((new_board, path + ' ' + direction))

def swap(board, direction):
    blank_row, blank_col = next(i for i, row in enumerate(board) if '_' in row)
    blank_col = row.index('_')
    if direction == 'up-right':
        new_row, new_col = blank_row - 1, blank_col + 1
    elif direction == 'down-right':
        new_row, new_col = blank_row + 1, blank_col + 1
    elif direction == 'up-left':
        new_row, new_col = blank_row - 1, blank_col - 1
    elif direction == 'down-left':
        new_row, new_col = blank_row + 1, blank_col - 1
    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
        new_board = [row.copy() for row in board]
        new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
        return new_board, new_path
    return board, path

init_board = [['i', 's', 'n', 'i', 'a', 'h'], ['l', 'p', 'e', 'a', 'r', 'c'], ['_', 'c', 'e', 'e', 'n', 'd'], ['e', 'v', 'e', 'r', 'l', 'y']]
print(bfs(init_board))
