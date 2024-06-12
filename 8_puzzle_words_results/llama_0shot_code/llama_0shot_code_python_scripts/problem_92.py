
from collections import deque

def bfs(init_board, words):
    moves = {0: 'up-right', 1: 'down-right', 2: 'up-left', 3: 'down-left'}
    visited = set()
    queue = deque([(init_board, '', 0)])  # board, actions, depth
    target = ','.join(words)

    while queue:
        board, actions, depth = queue.popleft()
        state = ''.join(board)
        if state in visited:
            continue
        visited.add(state)
        if state == target:
            return actions
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '_':
                    for k in range(4):
                        ni, nj = i + (-1 if k in [0, 2] else 1), j + (-1 if k in [0, 1] else 1)
                        if 0 <= ni < len(board) and 0 <= nj < len(board[i]):
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            queue.append((new_board, actions + ' ' + moves[k] if actions else moves[k], depth + 1))
    return None

init_board = [['e', 's', '_', 'r', 'k', 'w'], ['b', 'c', 'd', 'd', 'r', 'a'], ['c', 'u', 'e', 'c', 'e', 's'],
              ['b', 'r', 'n', 'h', 'e', 'a'], ['h', 'o', 'e', 'k', 'r', 'r']]
words = ['shrew', 'bedark', 'curcas', 'bender', 'hocker']

print(bfs(init_board, words))
