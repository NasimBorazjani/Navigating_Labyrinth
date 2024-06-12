
from collections import deque

def bfs(board, words):
    initial_board = tuple(map(tuple, board))
    initial_state = (initial_board, '_')
    target_state = (tuple(map(tuple, words)), '_')
    visited = set()
    queue = deque([([], initial_state)])
    while queue:
        moves, (board, position) = queue.popleft()
        if (board, '_') == target_state:
            return moves
        if (board, position) not in visited:
            visited.add((board, position))
            row, col = position.index('_'), position.index('_')
            for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    new_board = list(map(list, board))
                    new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                    new_state = (tuple(map(tuple, new_board)), new_board[new_row][new_col])
                    queue.append((moves + [dr * dc], new_state))

words = [['r', 'a', 'f', 't', 'y'], ['l', 'a', 'p', 'p', 'e'], ['a', 'n', 'n', 'i', 'a'], ['l', 't', 'n', 'd', 's'], ['a', 'c', 'a', 'i', 'd']]
board = [['a', 'r', 'o', 'f', 'n', 'y'], ['l', 'g', 'p', 'p', 'e', 'a'], ['a', 'n', 'n', 'i', '_', 'a'], ['l', 't', 'n', 'd', 's', 'e'], ['a', 'c', 'a', 'i', 'd', 'a']]
print(bfs(board, words))
