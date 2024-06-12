
from collections import deque

def is_target(board, words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            if board[i][j] != words[i][j]:
                return False
    return True

def generate_next_states(board):
    next_states = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                        new_board = [list(row) for row in board]
                        new_board[i][j], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[i][j]
                        next_states.append((new_board, (i, j, new_x, new_y)))
    return next_states

def bfs(board, words):
    queue = deque([(board, [])])
    visited = set()
    while queue:
        current_board, path = queue.popleft()
        if is_target(current_board, words):
            return path
        for next_board, move in generate_next_states(current_board):
            if tuple(map(tuple, next_board)) not in visited:
                visited.add(tuple(map(tuple, next_board)))
                queue.append((next_board, path + [move]))

initial_board = [['o', 'a', 'u', 'o'], ['p', 'r', 'l', 'e'], ['f', 'a', '_', 'f'], ['m', 'k', 'd', 'd']]
words = ['ako', 'pole', 'raff', 'mudd']

print(bfs(initial_board, words))
