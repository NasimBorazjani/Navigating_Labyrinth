
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target):
    n, m = len(board), len(board[0])
    target = [list(word) for word in target]
    queue = deque([(board, [])])
    visited = set([str(board)])
    directions = [(1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left'), (-1, 1, 'up-right')]

    while queue:
        curr_board, path = queue.popleft()
        if curr_board == target:
            return path
        i, j = find_blank(curr_board)
        for di, dj, dir in directions:
            ni, nj = i + di, j + dj
            if is_valid(ni, nj, n, m):
                new_board = [row[:] for row in curr_board]
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                if str(new_board) not in visited:
                    queue.append((new_board, path + [dir]))
                    visited.add(str(new_board))

    return None

target = ['ned', 'wham', 'royt', 'hell', 'miek']
board = [['h', 'n', '_', 'd'], ['w', 'r', 'a', 'e'], ['e', 'o', 'y', 't'], ['h', 'e', 'l', 'm'], ['m', 'i', 'l', 'k']]
print(bfs(board, target))
