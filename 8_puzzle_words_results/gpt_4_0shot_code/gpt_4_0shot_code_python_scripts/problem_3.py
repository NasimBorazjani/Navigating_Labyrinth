
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def get_neighbors(i, j):
    return [(i-1, j+1), (i+1, j+1), (i-1, j-1), (i+1, j-1)]

def swap(board, i1, j1, i2, j2):
    new_board = [row[:] for row in board]
    new_board[i1][j1], new_board[i2][j2] = new_board[i2][j2], new_board[i1][j1]
    return new_board

def sort_the_chars(board, target):
    n, m = len(board), len(board[0])
    target_board = [list(word) for word in target]
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        curr_board, path = queue.popleft()
        if curr_board == target_board:
            return path
        i, j = find_blank(curr_board)
        for ni, nj in get_neighbors(i, j):
            if is_valid(ni, nj, n, m):
                new_board = swap(curr_board, i, j, ni, nj)
                if str(new_board) not in visited:
                    queue.append((new_board, path + [(i, j, ni, nj)]))
                    visited.add(str(new_board))
    return None

board = [['v', 't', 'u', 'i'], ['o', 'w', 'e', 'i'], ['y', 'd', '_', 'c'], ['d', 'i', 'e', 'm']]
target = ['twi', 'ovey', 'udic', 'diem']
print(sort_the_chars(board, target))
