
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

def is_goal(board, target):
    return [''.join(row) for row in board] == target

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([''.join(''.join(row) for row in board)])
    while queue:
        board, actions = queue.popleft()
        if is_goal(board, target):
            return actions
        i, j = find_blank(board)
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                new_board = swap_blank(board, i, j, di, dj)
                new_state = ''.join(''.join(row) for row in new_board)
                if new_state not in visited:
                    queue.append((new_board, actions + [action]))
                    visited.add(new_state)

target = ['guha', 'nisus', 'uncap', 'jough']
board = [['i', 'g', 'u', 'h', 'a'], ['n', 'o', 's', 'u', 's'], ['c', 'n', 'g', 'a', '_'], ['j', 'u', 'u', 'p', 'h']]
print(bfs(board, target))
