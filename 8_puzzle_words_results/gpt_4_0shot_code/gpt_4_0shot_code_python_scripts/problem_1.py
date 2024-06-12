
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap(board, i, j, di, dj):
    new_board = [row[:] for row in board]
    new_board[i][j], new_board[i+di][j+dj] = new_board[i+di][j+dj], new_board[i][j]
    return new_board

def is_sorted(board, target):
    return [''.join(row) for row in board] == target

def bfs(board, target):
    queue = deque([(board, [])])
    seen = set([str(board)])
    while queue:
        board, path = queue.popleft()
        if is_sorted(board, target):
            return path
        i, j = find_blank(board)
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                new_board = swap(board, i, j, di, dj)
                if str(new_board) not in seen:
                    queue.append((new_board, path + [direction]))
                    seen.add(str(new_board))

board = [['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r']]
target = ['cam', 'hill', 'pray', 'doer']
print(bfs(board, target))
