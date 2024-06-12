
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
    queue = deque([(board, [], find_blank(board))])
    visited = set([str(board)])

    while queue:
        curr_board, path, blank = queue.popleft()
        if curr_board == target:
            return path

        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            new_i, new_j = blank[0] + di, blank[1] + dj
            if is_valid(new_i, new_j, n, m):
                new_board = [row[:] for row in curr_board]
                new_board[blank[0]][blank[1]], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[blank[0]][blank[1]]
                if str(new_board) not in visited:
                    queue.append((new_board, path + [direction], (new_i, new_j)))
                    visited.add(str(new_board))

    return []

target = ['echo', 'metin', 'perch', 'tulip', 'mulga']
board = [['e', 'e', 'l', 'h', 'o'], ['m', 'r', 't', 'u', 'n'], ['p', 'e', '_', 'c', 'i'], ['t', 'c', 'l', 'h', 'p'], ['m', 'u', 'i', 'g', 'a']]
print(bfs(board, target))
