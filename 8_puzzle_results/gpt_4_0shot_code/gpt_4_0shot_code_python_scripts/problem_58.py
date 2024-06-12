
from copy import deepcopy

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def solve_puzzle(board):
    goal = [[94, 91, 92, 86], [75, 73, 58, 46], [12, 10, 6, '_']]
    moves = []
    while board != goal:
        ei, ej = find_empty(board)
        if ei != 2:
            swap(board, ei, ej, ei+1, ej)
            moves.append(board[ei][ej])
        elif ej != 3:
            swap(board, ei, ej, ei, ej+1)
            moves.append(board[ei][ej])
        else:
            swap(board, ei, ej, ei-1, ej)
            moves.append(board[ei][ej])
    return moves

initial_state = [[94, 91, 92, 46], [6, 86, '_', 10], [12, 58, 73, 75]]
print(solve_puzzle(initial_state))
