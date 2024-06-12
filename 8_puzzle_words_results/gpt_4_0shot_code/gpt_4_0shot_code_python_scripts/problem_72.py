
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, pos, direction):
    i, j = pos
    new_board = [row[:] for row in board]
    if direction == 'up-right':
        new_board[i][j], new_board[i-1][j+1] = new_board[i-1][j+1], new_board[i][j]
    elif direction == 'down-right':
        new_board[i][j], new_board[i+1][j+1] = new_board[i+1][j+1], new_board[i][j]
    elif direction == 'up-left':
        new_board[i][j], new_board[i-1][j-1] = new_board[i-1][j-1], new_board[i][j]
    elif direction == 'down-left':
        new_board[i][j], new_board[i+1][j-1] = new_board[i+1][j-1], new_board[i][j]
    return new_board

def is_sorted(board, target):
    return [''.join(row) for row in board] == target

def sort_board(board, target):
    queue = deque([(board, [])])
    visited = set()
    while queue:
        board, path = queue.popleft()
        if is_sorted(board, target):
            return path
        blank_pos = find_blank(board)
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_board = swap(board, blank_pos, direction)
            if str(new_board) not in visited:
                queue.append((new_board, path + [direction]))
                visited.add(str(new_board))

board = [['o', 'l', '_', 't'], ['p', 'r', 'o', 'a'], ['e', 'i', 'k', 'k'], ['c', 'i', 'k', 'a'], ['s', 'l', 'r', 'm']]
target = ['lit', 'poor', 'kirk', 'cake', 'slam']
print(sort_board(board, target))
