
from collections import deque

def get_blank_pos(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def get_possible_moves(pos):
    x, y = pos
    moves = []
    if x > 0 and y < len(board[0]) - 1:
        moves.append((x - 1, y + 1, 'up-right'))
    if x < len(board) - 1 and y < len(board[0]) - 1:
        moves.append((x + 1, y + 1, 'down-right'))
    if x > 0 and y > 0:
        moves.append((x - 1, y - 1, 'up-left'))
    if x < len(board) - 1 and y > 0:
        moves.append((x + 1, y - 1, 'down-left'))
    return moves

def swap(board, pos1, pos2):
    board = [list(row) for row in board]
    board[pos1[0]][pos1[1]], board[pos2[0]][pos2[1]] = board[pos2[0]][pos2[1]], board[pos1[0]][pos1[1]]
    return [tuple(row) for row in board]

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([board])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank_pos = get_blank_pos(state)
        for move in get_possible_moves(blank_pos):
            new_state = swap(state, blank_pos, move[:2])
            if new_state not in visited:
                queue.append((new_state, path + [move[2]]))
                visited.add(new_state)

board = [('i', 's', 'n', 'i', 'a', 'h'), ('l', 'p', 'e', 'a', 'r', 'c'), ('_', 'c', 'e', 'e', 'n', 'd'), ('e', 'v', 'e', 'r', 'l', 'y')]
target = [('s', 'a', 'i', 'p', 'h', '_'), ('l', 'i', 'e', 'r', 'r', 'e'), ('a', 'c', 'c', 'e', 'n', 'd'), ('e', 'v', 'e', 'n', 'l', 'y')]
print(bfs(board, target))
