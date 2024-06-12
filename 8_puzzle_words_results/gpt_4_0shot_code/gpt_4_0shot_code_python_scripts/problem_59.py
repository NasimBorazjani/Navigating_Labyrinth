
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def get_neighbors(i, j, n, m):
    neighbors = []
    if i > 0 and j < m - 1:
        neighbors.append((i - 1, j + 1, 'up-right'))
    if i < n - 1 and j < m - 1:
        neighbors.append((i + 1, j + 1, 'down-right'))
    if i > 0 and j > 0:
        neighbors.append((i - 1, j - 1, 'up-left'))
    if i < n - 1 and j > 0:
        neighbors.append((i + 1, j - 1, 'down-left'))
    return neighbors

def bfs(board, target):
    n, m = len(board), len(board[0])
    queue = deque([(board, [], find_blank(board))])
    visited = set([str(board)])
    while queue:
        curr_board, path, blank = queue.popleft()
        if curr_board == target:
            return path
        i, j = blank
        for x, y, direction in get_neighbors(i, j, n, m):
            new_board = [row[:] for row in curr_board]
            new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
            if str(new_board) not in visited:
                queue.append((new_board, path + [direction], (x, y)))
                visited.add(str(new_board))
    return []

initial_board = [['r', 'f', '_', 'e'], ['t', 'a', 'a', 'f'], ['a', 'e', 'f', 't'], ['f', 'i', 'n', 'h'], ['d', 'a', 'e', 'f']]
target_words = [['f', 'a', 'e', '_'], ['t', 'r', 'a', 'h'], ['f', 'e', 'a', 't'], ['f', 'i', 'n', 'e'], ['d', 'a', 'f', 'f']]
print(bfs(initial_board, target_words))
