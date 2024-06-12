
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def valid_move(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target):
    moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    directions = ['down-right', 'up-left', 'down-left', 'up-right']
    queue = deque([(board, [], find_blank(board))])
    visited = set()

    while queue:
        curr_board, curr_moves, blank_pos = queue.popleft()
        if curr_board == target:
            return curr_moves
        for move, direction in zip(moves, directions):
            new_i, new_j = blank_pos[0] + move[0], blank_pos[1] + move[1]
            if valid_move(new_i, new_j, len(board), len(board[0])):
                new_board = [row[:] for row in curr_board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[blank_pos[0]][blank_pos[1]]
                new_board_tuple = tuple(tuple(row) for row in new_board)
                if new_board_tuple not in visited:
                    queue.append((new_board, curr_moves + [direction], (new_i, new_j)))
                    visited.add(new_board_tuple)

board = [['l', 'a', 'd', 'd', 'e', 'd'], ['a', 'h', 't', 'g', 'e', 'a'], ['_', 'n', 'd', 'i', 'r', 'n'], ['p', 'a', 't', 'i', 'o', 'n']]
target = [['_', 'a', 'd', 'd', 'e', 'd'], ['a', 'l', 't', 'h', 'e', 'a'], ['i', 'n', 'd', 'i', 'g', 'n'], ['p', 'a', 't', 'r', 'o', 'n']]
print(bfs(board, target))
