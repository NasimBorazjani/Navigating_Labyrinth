
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, i1, j1, i2, j2):
    new_board = [row[:] for row in board]
    new_board[i1][j1], new_board[i2][j2] = new_board[i2][j2], new_board[i1][j1]
    return new_board

def neighbors(i, j):
    return [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]

def bfs(board, target):
    queue = deque([(board, [])])
    seen = set([str(board)])
    while queue:
        board, path = queue.popleft()
        if board == target:
            return path
        i, j = find_blank(board)
        for ni, nj in neighbors(i, j):
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                new_board = swap(board, i, j, ni, nj)
                if str(new_board) not in seen:
                    queue.append((new_board, path + [(i, j, ni, nj)]))
                    seen.add(str(new_board))

initial = [['u', 'r', 'a', 'n', 'e'], ['s', 'l', 'r', 'i', 's'], ['a', 'i', '_', 'e', 'e'], ['b', 'o', 'k', 'b', 'l'], ['s', 'k', 'r', 'f', 'f']]
target = [['_', 'r', 'a', 'n', 'e'], ['s', 'u', 'r', 'e', 's'], ['l', 'i', 'b', 'e', 'r'], ['b', 'i', 'k', 'o', 'l'], ['s', 'k', 'a', 'f', 'f']]
print(bfs(initial, target))
