
from collections import deque

def get_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def get_target(board, target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == target:
                return (i, j)

def swap(board, pos1, pos2):
    board[pos1[0]][pos1[1]], board[pos2[0]][pos2[1]] = board[pos2[0]][pos2[1]], board[pos1[0]][pos1[1]]
    return board

def get_moves(pos):
    moves = [(pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1), (pos[0] - 1, pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
    return [move for move in moves if 0 <= move[0] < 4 and 0 <= move[1] < 4]

def bfs(board, target):
    queue = deque([(board, [])])
    while queue:
        board, path = queue.popleft()
        blank = get_blank(board)
        if board == target:
            return path
        for move in get_moves(blank):
            new_board = [row[:] for row in board]
            new_board = swap(new_board, blank, move)
            queue.append((new_board, path + [move]))

board = [['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
target = [['a', 'n', 'n', '_'], ['b', 'i', 'r', 'k'], ['t', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
print(bfs(board, target))
