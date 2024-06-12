
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def valid_moves(i, j, n, m):
    moves = []
    if i > 0 and j < m - 1:
        moves.append((i - 1, j + 1, 'up-right'))
    if i < n - 1 and j < m - 1:
        moves.append((i + 1, j + 1, 'down-right'))
    if i > 0 and j > 0:
        moves.append((i - 1, j - 1, 'up-left'))
    if i < n - 1 and j > 0:
        moves.append((i + 1, j - 1, 'down-left'))
    return moves

def sort_the_chars(board, target):
    n, m = len(board), len(board[0])
    target = [list(word) for word in target]
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        curr_board, path = queue.popleft()
        if curr_board == target:
            return path
        i, j = find_blank(curr_board)
        for x, y, direction in valid_moves(i, j, n, m):
            new_board = [row[:] for row in curr_board]
            new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
            if str(new_board) not in visited:
                queue.append((new_board, path + [direction]))
                visited.add(str(new_board))
    return None

board = [['u', 'n', 'a', 'b'], ['g', 'b', 'l', 'l'], ['a', 'o', '_', 'k'], ['t', 'o', 'l', 'c'], ['f', 'l', 'o', 'b']]
target = ['nab', 'gull', 'book', 'talc', 'flob']
print(sort_the_chars(board, target))
