
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def next_states(board, i, j):
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
    target = target.split(', ')
    queue = deque([(board, [])])
    seen = set()
    while queue:
        state, path = queue.popleft()
        if is_goal(state, target):
            return path
        for next_state in next_states(state, *find_blank(state)):
            str_state = str(next_state)
            if str_state not in seen:
                seen.add(str_state)
                queue.append((next_state, path + [next_state]))

board = [['t', 'p', 'c', 'p', 'o', 'y'], ['s', 'e', 'o', 't', 'k', 's'], ['p', 'i', 'w', 't', '_', 'l'], ['s', 'n', 'a', 'y', 'h', 'a'], ['c', 'a', 'e', 'c', 'p', 'n']]
target = 'peppy, stocky, pistol, swathe, cancan'
print(solve(board, target))
