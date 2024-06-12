
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap_blank(board, i, j, di, dj):
    new_board = [row[:] for row in board]
    new_board[i][j], new_board[i+di][j+dj] = new_board[i+di][j+dj], new_board[i][j]
    return new_board

def is_goal(board, words):
    return [''.join(row) for row in board] == words

def bfs(board, words):
    moves = [(1, -1), (-1, 1), (1, 1), (-1, -1)]
    directions = ['down-left', 'up-right', 'down-right', 'up-left']
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        board, actions = queue.popleft()
        if is_goal(board, words):
            return actions
        i, j = find_blank(board)
        for move, direction in zip(moves, directions):
            di, dj = move
            if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                new_board = swap_blank(board, i, j, di, dj)
                if str(new_board) not in visited:
                    queue.append((new_board, actions + [direction]))
                    visited.add(str(new_board))
    return []

words = ['man', 'cute', 'dazy', 'down', 'oryx']
board = [['u', 'm', 'a', 'n'], ['c', 'd', 't', 'e'], ['o', 'a', '_', 'y'], ['d', 'n', 'w', 'y'], ['o', 'r', 'z', 'x']]
print(bfs(board, words))
