
from collections import deque

def bfs(init_board, words):
    dirs = [(-1, 1), (1, 1), (-1, -1), (1, -1)]  # up-right, down-right, up-left, down-left
    queue = deque([(init_board, [])])  # (board, swaps)
    visited = set()

    while queue:
        board, swaps = queue.popleft()
        key = str(board)
        if key in visited:
            continue
        visited.add(key)

        if board[0] == list(words[0]) and board[1] == list(words[1]) and board[2] == list(words[2]) and board[3] == list(words[3]) and board[4] == list(words[4]):
            return swaps

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '_':
                    for dir in dirs:
                        ni, nj = i + dir[0], j + dir[1]
                        if 0 <= ni < len(board) and 0 <= nj < len(board[i]):
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            queue.append((new_board, swaps + [dir]))

    return None

init_board = [['o', 'l', '_', 't'], ['p', 'r', 'o', 'a'], ['e', 'i', 'k', 'k'], ['c', 'i', 'k', 'a'], ['s', 'l', 'r', 'm']]
words = ['lit', 'poor', 'kirk', 'cake', 'slam']
print(bfs(init_board, words))
