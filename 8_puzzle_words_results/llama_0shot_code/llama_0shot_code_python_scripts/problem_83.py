
from collections import deque

def get_neighbors(board):
    n, m = len(board), len(board[0])
    blank_row, blank_col = None, None
    for i in range(n):
        for j in range(m):
            if board[i][j] == '_':
                blank_row, blank_col = i, j
                break
        else:
            continue
        break
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = blank_row + dr, blank_col + dc
        if 0 <= nr < n and 0 <= nc < m:
            new_board = [row.copy() for row in board]
            new_board[blank_row][blank_col], new_board[nr][nc] = new_board[nr][nc], new_board[blank_row][blank_col]
            neighbors.append((new_board, dr, dc))
    return neighbors

def is_goal(board, words):
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            if board[i][j] != char:
                return False
    return True

def solve(board, words):
    queue = deque([(board, [])])
    visited = set()
    while queue:
        current_board, swaps = queue.popleft()
        if is_goal(current_board, words):
            return swaps
        for new_board, dr, dc in get_neighbors(current_board):
            if tuple(map(tuple, new_board)) not in visited:
                visited.add(tuple(map(tuple, new_board)))
                new_swaps = swaps + [dr, dc]
                queue.append((new_board, new_swaps))

initial_board = [['u', 'r', 'a', 'n', 'e'], ['s', 'l', 'r', 'i', 's'], ['a', 'i', '_', 'e', 'e'], ['b', 'o', 'k', 'b', 'l'], ['s', 'k', 'r', 'f', 'f']]
words = ['rane', 'sures', 'liber', 'bikol', 'skaff']

print(solve(initial_board, words))
