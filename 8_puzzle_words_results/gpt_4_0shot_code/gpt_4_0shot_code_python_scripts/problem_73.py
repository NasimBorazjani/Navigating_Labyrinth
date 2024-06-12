
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
    start = find_blank(board)
    queue = deque([(start, board, [])])
    visited = set([str(board)])
    dirs = [(1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'up-right'), (1, -1, 'down-left')]

    while queue:
        (x, y), cur_board, path = queue.popleft()
        if cur_board == target:
            return path
        for dx, dy, dir in dirs:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n, m):
                new_board = [row[:] for row in cur_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                if str(new_board) not in visited:
                    queue.append(((nx, ny), new_board, path + [dir]))
                    visited.add(str(new_board))

    return []

target = ['trag', 'hoped', 'shelf', 'neath', 'farse']
board = [['o', 't', 'f', 'a', 'g'], ['h', 'r', 'p', 'r', 'd'], ['s', 'h', '_', 'l', 't'], ['n', 'e', 'a', 'e', 'h'], ['f', 'a', 'e', 's', 'e']]
print(bfs(board, target))
