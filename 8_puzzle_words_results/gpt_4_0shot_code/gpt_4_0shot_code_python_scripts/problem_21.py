
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap_blank(board, i, j, di, dj):
    new_board = [row[:] for row in board]
    new_board[i][j], new_board[i+di][j+dj] = new_board[i+di][j+dj], new_board[i][j]
    return new_board

def is_goal(board, words):
    return [''.join(row) for row in board] == words

def bfs(board, words):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        board, actions = queue.popleft()
        if is_goal(board, words):
            return actions
        i, j = find_blank(board)
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                new_board = swap_blank(board, i, j, di, dj)
                if str(new_board) not in visited:
                    queue.append((new_board, actions + [action]))
                    visited.add(str(new_board))
    return []

words = ['poss', 'smoke', 'casel', 'hiram']
board = [['m', 'p', 'l', 's', 's'], ['s', 'a', 'o', 's', 'e'], ['c', 'a', '_', 'e', 'k'], ['h', 'i', 'r', 'o', 'm']]
print(bfs(board, words))
