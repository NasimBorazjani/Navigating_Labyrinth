
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def valid_move(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target):
    n, m = len(board), len(board[0])
    start = find_blank(board)
    queue = deque([(start, board, [])])
    visited = set([str(board)])
    moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    directions = ['down-right', 'up-left', 'down-left', 'up-right']

    while queue:
        (x, y), cur_board, path = queue.popleft()
        if cur_board == target:
            return path
        for move, direction in zip(moves, directions):
            nx, ny = x + move[0], y + move[1]
            if valid_move(nx, ny, n, m):
                new_board = [row[:] for row in cur_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                if str(new_board) not in visited:
                    queue.append(((nx, ny), new_board, path + [direction]))
                    visited.add(str(new_board))

    return []

target = [['s', 'n', 'i', 'p', '_'], ['s', 'c', 'o', 'o', 'n'], ['c', 'u', 'b', 'e', 'r'], ['a', 'r', 't', 'i', 'e'], ['p', 'e', 'n', 't', 'a']]
board = [['c', 's', 'n', 'i', 'p'], ['s', 'o', 'o', 'r', 'n'], ['c', 'u', 'i', 'e', '_'], ['a', 'n', 't', 'b', 'e'], ['p', 'e', 'r', 't', 'a']]
print(bfs(board, target))
