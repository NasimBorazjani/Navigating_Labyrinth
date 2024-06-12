
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, pos, direction):
    i, j = pos
    if direction == 'up-right' and i > 0 and j < len(board[0]) - 1:
        board[i][j], board[i-1][j+1] = board[i-1][j+1], board[i][j]
    elif direction == 'down-right' and i < len(board) - 1 and j < len(board[0]) - 1:
        board[i][j], board[i+1][j+1] = board[i+1][j+1], board[i][j]
    elif direction == 'up-left' and i > 0 and j > 0:
        board[i][j], board[i-1][j-1] = board[i-1][j-1], board[i][j]
    elif direction == 'down-left' and i < len(board) - 1 and j > 0:
        board[i][j], board[i+1][j-1] = board[i+1][j-1], board[i][j]

def is_sorted(board, target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != target[i][j]:
                return False
    return True

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        board, path = queue.popleft()
        if is_sorted(board, target):
            return path
        blank_pos = find_blank(board)
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_board = [row[:] for row in board]
            swap(new_board, blank_pos, direction)
            if str(new_board) not in visited:
                queue.append((new_board, path + [direction]))
                visited.add(str(new_board))

board = [['o', 'j', '_', 'h', 'u'], ['w', 'l', 'r', 'e', 'y'], ['n', 'i', 'l', 't', 'a'], ['i', 'y', 'i', 'm', 'l']]
target = [['j', 'e', 'h', 'u', '_'], ['w', 'o', 'r', 'm', 'y'], ['l', 'i', 'n', 't', 'y'], ['i', 'l', 'i', 'a', 'l']]
print(bfs(board, target))
