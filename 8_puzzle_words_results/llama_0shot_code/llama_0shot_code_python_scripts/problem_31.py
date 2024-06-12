
from collections import deque

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target_words):
    n, m = len(board), len(board[0])
    target_boards = [[''.join(row) for row in board]]
    for word in target_words:
        target_boards.append(word)
    visited = set([''.join(row) for row in board])
    q = deque([([''.join(row) for row in board], [])])
    while q:
        curr_board, swaps = q.popleft()
        for i in range(n):
            for j in range(m):
                if curr_board[i][j] == '_':
                    for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        ni, nj = i + di, j + dj
                        if is_valid(ni, nj, n, m):
                            new_board = [list(row) for row in curr_board]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            new_board_str = [''.join(row) for row in new_board]
                            if ''.join(new_board_str) in target_boards:
                                return swaps + [new_board_str.index(''.join(new_board))]
                            if ''.join(new_board_str) not in visited:
                                visited.add(''.join(new_board_str))
                                q.append((new_board_str, swaps + [target_boards.index(''.join(new_board))]))

initial_board = [['t', 'd', 'u', 'k', 'e'], ['a', 'a', 'o', 'l', 'l'], ['a', 'm', '_', 'z', 'i'], ['n', 'e', 'u', 'y', 'n']]
target_words = ['dyke', 'atoll', 'amuze', 'niuan']
print(bfs(initial_board, target_words))
