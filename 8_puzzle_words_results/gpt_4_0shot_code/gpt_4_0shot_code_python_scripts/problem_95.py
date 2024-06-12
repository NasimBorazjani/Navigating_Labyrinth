
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        board, path = queue.popleft()
        if board == target:
            return path
        i, j = find_blank(board)
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                swap(board, i, j, ni, nj)
                if str(board) not in visited:
                    queue.append((board[:], path + [direction]))
                    visited.add(str(board))
                swap(board, i, j, ni, nj)
    return []

initial_board = [['y', 't', 's', 'n', 'a', 'r'], ['m', 'r', 'r', 't', 'o', 'e'], ['l', 'o', '_', 'd', 'l', 'n'], ['e', 'u', 'v', 'i', 'r', 'a'], ['h', 'e', 'l', 'm', 'a', 'n']]
target_board = [['_', 't', 'u', 'n', 'e', 'r'], ['m', 'y', 'r', 't', 'o', 'l'], ['s', 'o', 'l', 'd', 'a', 'n'], ['e', 'l', 'v', 'i', 'r', 'a'], ['h', 'e', 'r', 'm', 'a', 'n']]
print(bfs(initial_board, target_board))
