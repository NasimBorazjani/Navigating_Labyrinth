
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    while queue:
        current_board, direction = queue.popleft()
        current_str = ''.join([''.join(row) for row in current_board])
        if current_str == ''.join(words):
            return direction
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current_board) and 0 <= ny < len(current_board[0]):
                            new_board = [list(row) for row in current_board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_state = (tuple(tuple(row) for row in new_board), (i, j, nx, ny))
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append(new_state)
    return None

initial_board = [['u', 's', 'o', 'f', 't'], ['t', 'a', 'n', 'n', 'y'], ['a', 'p', '_', 'm', 'o'], ['f', 'u', 'r', 'a', 'm']]
target_words = ['soft', 'tunny', 'apama', 'forum']

print(bfs(initial_board, target_words))
