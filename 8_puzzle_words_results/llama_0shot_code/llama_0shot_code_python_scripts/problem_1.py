
from collections import deque

def is_solved(board, words):
    for i, word in enumerate(words):
        if board[i][:-1] != list(word) and board[i][1:] != list(word):
            return False
    return True

def get_neighbours(board):
    x, y = next((i, j) for i, row in enumerate(board) for j, c in enumerate(row) if c == '_')
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            new_board = [row.copy() for row in board]
            new_board[nx][ny], new_board[x][y] = new_board[x][y], new_board[nx][ny]
            yield (new_board, (nx - x, ny - y))

def solve(board, words):
    queue = deque([(board, [])])
    while queue:
        current_board, path = queue.popleft()
        if is_solved(current_board, words):
            return path
        for new_board, direction in get_neighbours(current_board):
            queue.append((new_board, path + [direction]))
    return None

initial_board = [['i', 'c', 'a', 'm'], ['h', 'p', 'l', 'o'], ['_', 'r', 'a', 'y'], ['d', 'l', 'e', 'r']]
target_words = ["cam", "hill", "pray", "doer"]

print(solve(initial_board, target_words))
