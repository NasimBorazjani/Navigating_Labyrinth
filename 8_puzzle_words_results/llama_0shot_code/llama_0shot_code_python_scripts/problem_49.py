
from collections import deque

def bfs(board, words):
    queue = deque([(board, words)])
    visited = set()
    while queue:
        current_board, current_words = queue.popleft()
        current_state = "".join(["".join(row) for row in current_board])
        if current_state not in visited:
            visited.add(current_state)
            if current_words == []:
                return current_state
            for i in range(len(current_board)):
                for j in range(len(current_board[i])):
                    if current_board[i][j] == '_':
                        for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                            new_i, new_j = i + di, j + dj
                            if 0 <= new_i < len(current_board) and 0 <= new_j < len(current_board[i]):
                                new_board = [row.copy() for row in current_board]
                                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                                queue.append((new_board, current_words[1:]))
    return None

initial_board = [['a', 'l', 'o', 'a', 'm', 'h'], ['f', 'e', 'n', 'n', 'a', 't'], ['t', 'r', 'a', 'g', '_', 'c'], ['c', 'i', 'r', 'a', 'n', 'e']]
words = ['leath', 'fanman', 'tragic', 'carone']

result = bfs(initial_board, words)
print(result)
