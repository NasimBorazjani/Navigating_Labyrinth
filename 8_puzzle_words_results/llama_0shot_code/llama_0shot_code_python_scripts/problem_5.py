
from collections import deque

def bfs(init_board, target_words):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up-right, down-right, up-left, down-left
    target_state = ''.join(target_words)
    queue = deque([(init_board, '', (0, 0))])  # (board, swaps, blank_position)
    visited = set()

    while queue:
        board, swaps, (x, y) = queue.popleft()
        state = ''.join([''.join(row) for row in board])
        if state == target_state:
            return swaps
        if state not in visited:
            visited.add(state)
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '_':
                    new_board = [row.copy() for row in board]
                    new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                    queue.append((new_board, swaps + (new_board[nx][ny],), (nx, ny)))

init_board = [['a', 's', 't', 'x'], ['t', 'r', 's', 'a'], ['s', 'u', '_', 'p'], ['c', 'a', 'd', 'e']]
target_words = ['sax', 'tass', 'turp', 'cade']
print(bfs(init_board, target_words))
