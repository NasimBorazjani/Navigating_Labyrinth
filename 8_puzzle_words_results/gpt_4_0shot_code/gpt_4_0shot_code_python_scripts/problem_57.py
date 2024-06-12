
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, i1, j1, i2, j2):
    new_board = [list(row) for row in board]
    new_board[i1][j1], new_board[i2][j2] = new_board[i2][j2], new_board[i1][j1]
    return tuple(map(tuple, new_board))

def bfs(initial_board, target_board):
    queue = deque([initial_board])
    visited = set([initial_board])
    prev = {initial_board: (None, None)}
    while queue:
        board = queue.popleft()
        if board == target_board:
            actions = []
            while board != initial_board:
                board, action = prev[board]
                actions.append(action)
            actions.reverse()
            return actions
        i, j = find_blank(board)
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                new_board = swap(board, i, j, i + di, j + dj)
                if new_board not in visited:
                    queue.append(new_board)
                    visited.add(new_board)
                    prev[new_board] = (board, action)

initial_board = (('u', 't', '_', 'e'), ('k', 'a', 'b', 'm'), ('n', 'e', 'o', 'g'), ('p', 'u', 's', 'o'), ('y', 'o', 'e', 'p'))
target_board = (('t', 'o', 'e', '_'), ('k', 'u', 'b', 'a'), ('m', 'e', 'n', 'g'), ('p', 'e', 's', 'o'), ('y', 'o', 'u', 'p'))
print(bfs(initial_board, target_board))
