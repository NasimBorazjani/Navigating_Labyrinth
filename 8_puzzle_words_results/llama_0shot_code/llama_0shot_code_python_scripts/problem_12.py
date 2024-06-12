
from collections import deque

def bfs(init_board):
    moves = deque([(init_board, '')])
    visited = set()
    while moves:
        board, path = moves.popleft()
        if board not in visited:
            visited.add(board)
            if board == [['h', 'a', 't'], ['a', 's', 'k', 'a'], ['t', 'l', 'i', '_'], ['m', 'd', 'n', 'g']]:
                return path
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '_':
                        for x, y in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                            new_i, new_j = i + x, j + y
                            if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                                new_board = [row.copy() for row in board]
                                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                                new_path = path + 'ur'[::-1] if x == -1 and y == 1 else 'dr'[::-1] if x == 1 and y == 1 else 'ul'[::-1] if x == -1 and y == -1 else 'dl'
                                moves.append((new_board, new_path))
    return None

init_board = [['k', 'h', 'a', 't'], ['s', 'a', 'a', 'a'], ['i', 'l', '_', 't'], ['m', 'g', 'n', 'd']]
print(bfs(init_board))
