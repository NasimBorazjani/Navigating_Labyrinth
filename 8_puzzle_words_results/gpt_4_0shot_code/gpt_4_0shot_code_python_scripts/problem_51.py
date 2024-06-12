
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
    queue = deque([(board, start, [])])
    visited = set([str(board)])
    directions = [(1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'up-right'), (1, -1, 'down-left')]

    while queue:
        curr_board, (x, y), path = queue.popleft()
        if curr_board == target:
            return path
        for dx, dy, dir in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n, m):
                new_board = [row[:] for row in curr_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                if str(new_board) not in visited:
                    queue.append((new_board, (nx, ny), path + [dir]))
                    visited.add(str(new_board))

    return []

board = [['l', 'b', 'l', 'u', 'i', 'e'], ['a', 't', 'g', 'n', 's', 'c'], ['l', 'a', 'o', 'u', '_', 'e'], ['n', 'i', 'n', 'p', 'o', 'n']]
target = ['biune', 'algist', 'palule', 'noncon']
print(bfs(board, target))
