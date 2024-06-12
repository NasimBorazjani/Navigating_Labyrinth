
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def generate_states(board, i, j):
    states = []
    directions = [(i-1, j+1, 'up-right'), (i+1, j+1, 'down-right'), (i-1, j-1, 'up-left'), (i+1, j-1, 'down-left')]
    for di, dj, direction in directions:
        if 0 <= di < len(board) and 0 <= dj < len(board[0]):
            new_board = [row[:] for row in board]
            swap(new_board, i, j, di, dj)
            states.append((new_board, direction))
    return states

def is_goal(board, target_words):
    return [''.join(row) for row in board] == target_words

def solve(board, target_words):
    queue = deque([(board, [])])
    visited = set()
    while queue:
        board, path = queue.popleft()
        if is_goal(board, target_words):
            return path
        i, j = find_blank(board)
        for new_board, direction in generate_states(board, i, j):
            new_board_tuple = tuple(tuple(row) for row in new_board)
            if new_board_tuple not in visited:
                queue.append((new_board, path + [direction]))
                visited.add(new_board_tuple)

initial_board = [['w', 'k', 'u', 'a', 'd', 'i'], ['s', 'a', 'a', 'r', 'm', 'y'], ['h', 'g', '_', 'i', 's', 'h'], ['w', 'h', 'e', 'a', 't', 'y']]
target_words = ['khadi', 'swarmy', 'aguish', 'wheaty']
print(solve(initial_board, target_words))
