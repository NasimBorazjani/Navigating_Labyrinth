
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
    directions = [(i-1, j+1), (i+1, j+1), (i-1, j-1), (i+1, j-1)]
    for di, dj in directions:
        if 0 <= di < len(board) and 0 <= dj < len(board[0]):
            new_board = [row[:] for row in board]
            swap(new_board, i, j, di, dj)
            states.append(new_board)
    return states

def is_goal(board, target):
    return [''.join(row) for row in board] == target

def solve(board, target):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        state, path = queue.popleft()
        if is_goal(state, target):
            return path
        i, j = find_blank(state)
        for new_state in generate_states(state, i, j):
            str_state = str(new_state)
            if str_state not in visited:
                visited.add(str_state)
                queue.append((new_state, path + [(i, j)]))
    return None

initial_board = [['i', 'e', 'k', 'k', 'a'], ['b', 'e', 'f', 'a', 'r'], ['g', 'a', '_', 'm', 'e'], ['d', 'i', 'n', 'k', 'a'], ['b', 'r', 'm', 't', 't']]
target_words = ['ekka', 'bifer', 'magma', 'dinka', 'brett']
print(solve(initial_board, target_words))
