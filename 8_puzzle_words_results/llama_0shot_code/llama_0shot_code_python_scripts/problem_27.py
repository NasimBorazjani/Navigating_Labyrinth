
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, [])])
    target = ''.join(words) + '.'
    while queue:
        current_board, swaps = queue.popleft()
        current_state = ''.join(current_board) + '.'
        if current_state == target:
            return swaps
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current_board) and 0 <= ny < len(current_board[0]):
                            new_board = [list(row) for row in current_board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_state = ''.join([''.join(row) for row in new_board]) + '.'
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_board, swaps + [(i, j, nx, ny)]))
    return None

initial_board = [['_', 'b', 'p', 'i', 's'], ['d', 'u', 'r', 'n', 'c'], ['l', 'i', 'o', 'e', 'n'], ['s', 'n', 'e', 'o', 't']]
words = ['bois', 'duroc', 'linen', 'spent']

swaps = bfs(initial_board, words)
print(swaps)
