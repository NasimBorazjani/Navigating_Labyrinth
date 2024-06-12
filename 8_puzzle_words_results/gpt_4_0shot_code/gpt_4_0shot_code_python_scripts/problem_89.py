
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def valid_move(i, j, direction):
    if direction == 'up-right' and i > 0 and j < len(board[0]) - 1:
        return True
    if direction == 'down-right' and i < len(board) - 1 and j < len(board[0]) - 1:
        return True
    if direction == 'up-left' and i > 0 and j > 0:
        return True
    if direction == 'down-left' and i < len(board) - 1 and j > 0:
        return True
    return False

def make_move(board, i, j, direction):
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

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        current_board, path = queue.popleft()
        if current_board == target:
            return path
        i, j = find_blank(current_board)
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            if valid_move(i, j, direction):
                new_board = make_move(current_board, i, j, direction)
                if str(new_board) not in visited:
                    queue.append((new_board, path + [direction]))
                    visited.add(str(new_board))
    return None

board = [['a', 'f', 'w', 'g', 'e'], ['p', 'f', 'l', 'm', 'y'], ['o', 'o', 'a', 'r', 'a'], ['g', 'a', 'm', 'e', 't'], ['p', 'u', '_', 'f', 'y']]
target = [['f', 'a', 'g', 'e', '_'], ['p', 'a', 'l', 'a', 'y'], ['m', 'o', 'w', 'r', 'a'], ['g', 'e', 'm', 'o', 't'], ['p', 'u', 'f', 'f', 'y']]
print(bfs(board, target))
