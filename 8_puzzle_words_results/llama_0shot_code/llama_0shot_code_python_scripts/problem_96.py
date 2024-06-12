
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    moves = {(0, 1): 'up-right', (0, -1): 'down-right', (1, 0): 'up-left', (-1, 0): 'down-left'}
    target = [''.join(word) for word in words]
    while queue:
        current_board, direction = queue.popleft()
        current_state = tuple(tuple(row) for row in current_board)
        if current_state not in visited:
            visited.add(current_state)
            if current_board[2][2] == '_':
                for dr, dc in moves:
                    nr, nc = 2 + dr, 2 + dc
                    if 0 <= nr < len(current_board) and 0 <= nc < len(current_board[0]) and current_board[nr][nc] == '_':
                        new_board = [list(row) for row in current_board]
                        new_board[2][2], new_board[nr][nc] = new_board[nr][nc], new_board[2][2]
                        new_board = [tuple(row) for row in new_board]
                        queue.append((new_board, moves[(dr, dc)]))
                        if new_board[2][2] == '_' and ''.join(new_board[2][:5]) in target:
                            return direction, new_board, target.index(''.join(new_board[2][:5])) + 1
            else:
                nr, nc = current_board[2].index('_')
                for dr, dc in moves:
                    if 0 <= nr + dr < len(current_board) and 0 <= nc + dc < len(current_board[0]) and current_board[nr + dr][nc + dc] == '_':
                        new_board = [list(row) for row in current_board]
                        new_board[nr][nc], new_board[nr + dr][nc + dc] = new_board[nr + dr][nc + dc], new_board[nr][nc]
                        new_board = [tuple(row) for row in new_board]
                        queue.append((new_board, moves[(dr, dc)]))
                        if new_board[2][2] == '_' and ''.join(new_board[2][:5]) in target:
                            return direction, new_board, target.index(''.join(new_board[2][:5])) + 1
    return None

initial_board = [['o', 's', 'n', 'e', 'd', 'a'], ['l', 'k', 'c', 'c', 'e', 'h'], ['t', 'o', '_', 'c', 'n', 'e'], ['c', 'i', 'l', 'a', 'i', 'c'], ['b', 'l', 'e', 'n', 'c', 'o']]
words = ['siena', 'locked', 'conche', 'celtic', 'blanco']

print(bfs(initial_board, words))
