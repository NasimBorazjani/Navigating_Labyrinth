
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    moves = {(0, 1): 'up-right', (1, 0): 'down-right', (0, -1): 'up-left', (-1, 0): 'down-left'}
    while queue:
        current_board, direction = queue.popleft()
        current_str = ''.join([''.join(row) for row in current_board])
        if current_str == ''.join(words):
            return direction
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for move in moves:
                        new_i, new_j = i + move[0], j + move[1]
                        if 0 <= new_i < len(current_board) and 0 <= new_j < len(current_board[0]) and current_board[new_i][new_j] != '_':
                            new_board = [row.copy() for row in current_board]
                            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                            new_state = (tuple(tuple(row) for row in new_board), (new_i - i, new_j - j))
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append(new_state)
    return None

words = ['gong', 'clown', 'brent', 'dewax', 'thorp']
board = [['l', 'g', '_', 'a', 'n'], ['c', 'o', 'o', 'e', 'n'], ['e', 'r', 'n', 't', ''], ['d', 'b', 'w', 'o', 'x'], ['t', 'h', 'w', 'r', 'p']]
print(bfs(board, words))
