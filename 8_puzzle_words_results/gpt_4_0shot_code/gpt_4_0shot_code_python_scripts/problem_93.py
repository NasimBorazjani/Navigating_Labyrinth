
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
    start = find_blank(board)
    queue = deque([(start, board, [])])
    visited = set([str(board)])
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    dir_names = ['down-right', 'up-left', 'down-left', 'up-right']

    while queue:
        (x, y), cur_board, path = queue.popleft()
        if cur_board == target:
            return path
        for d, dir_name in zip(dirs, dir_names):
            nx, ny = x + d[0], y + d[1]
            if is_valid(nx, ny, n, m):
                new_board = [row[:] for row in cur_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                if str(new_board) not in visited:
                    queue.append(((nx, ny), new_board, path + [dir_name]))
                    visited.add(str(new_board))

    return []

target = [['h', 'e', 'l', 'e', 'n'], ['a', 'd', 'e', 'l', 'e', 'a'], ['b', 'u', 'm', 'b', 'l', 'e'], ['i', 'o', 'd', 'i', 's', 'm'], ['t', 'r', 'u', 'l', 'l', 'o']]
board = [['d', 'h', '_', 'l', 'e', 'n'], ['a', 'a', 'e', 'b', 'e', 'u'], ['m', 'u', 'i', 'b', 'e', 'e'], ['i', 'o', 'd', 'm', 's', 'l'], ['t', 'r', 'l', 'l', 'l', 'o']]
print(bfs(board, target))
