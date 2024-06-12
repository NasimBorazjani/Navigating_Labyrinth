
from collections import deque

def bfs(init_board, target_words):
    visited = set()
    queue = deque([(init_board, [])])
    target_board = [''.join(target_words[i:i+len(init_board[0])-1]) for i in range(0, len(target_words), len(init_board[0])-1)]
    while queue:
        board, swaps = queue.popleft()
        key = ''.join(board)
        if key in visited:
            continue
        visited.add(key)
        if board == target_board:
            return swaps
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            queue.append(([''.join(row) for row in new_board], swaps + [(i, j, nx, ny)]))

init_board = [['r', 'f', '_', 'e'], ['t', 'a', 'a', 'f'], ['a', 'e', 'f', 't'], ['f', 'i', 'n', 'h'], ['d', 'a', 'e', 'f']]
target_words = ['fae', 'trah', 'feat', 'fine', 'daff']
print(bfs(init_board, target_words))
