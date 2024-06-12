
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    while queue:
        current_board, direction = queue.popleft()
        current_words = ''.join([''.join(row) for row in current_board])
        if current_words == ''.join(words):
            return direction
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current_board) and 0 <= ny < len(current_board[0]):
                            new_board = [row.copy() for row in current_board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_direction = (i, j, nx, ny)
                            if (tuple(new_board), new_direction) not in visited:
                                visited.add((tuple(new_board), new_direction))
                                queue.append((new_board, new_direction))
    return None

initial_board = [['h', 'b', 'c', 't', 'h'], ['k', 'n', 'i', 'o', 'a'], ['a', 's', '_', 'o', 'a'], ['c', 'l', 'a', 's', 't']]
target_words = ['bath', 'khila', 'ascon', 'coast']

directions = bfs(initial_board, target_words)
print(directions)
