
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, swaps = queue.popleft()
        if current == target:
            return swaps
        for direction in get_possible_swaps(current):
            next_board, next_swaps = move(current, direction)
            if next_board not in visited:
                visited.add(next_board)
                queue.append((next_board, swaps + [direction]))

def get_possible_swaps(board):
    row, col = get_blank_position(board)
    directions = []
    if row > 0 and col > 0:
        directions.append('up-left')
    if row > 0 and col < len(board[0]) - 1:
        directions.append('up-right')
    if row < len(board) - 1 and col > 0:
        directions.append('down-left')
    if row < len(board) - 1 and col < len(board[0]) - 1:
        directions.append('down-right')
    return directions

def move(board, direction):
    row, col = get_blank_position(board)
    if direction == 'up-left':
        row -= 1
        col -= 1
    elif direction == 'up-right':
        row -= 1
        col += 1
    elif direction == 'down-left':
        row += 1
        col -= 1
    elif direction == 'down-right':
        row += 1
        col += 1
    new_board = swap_blank(board, (row, col))
    return new_board, direction

def get_blank_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap_blank(board, new_position):
    new_board = [row.copy() for row in board]
    new_board[new_position[0]][new_position[1]] = '_'
    new_board[get_blank_position(board)[0]][get_blank_position(board)[1]] = board[new_position[0]][new_position[1]]
    return new_board

initial_board = [['h', 'k', 't', 'n'], ['k', 'e', 'a', 'k'], ['e', 'i', '_', 'l'], ['w', 'l', 'n', 't']]
target_board = [['_', 'k', 'e', 'n'], ['k', 'h', 't', 'a'], ['i', 'l', 'l', 'w'], ['e', 't', 'n', 'k']]

print(bfs(initial_board, target_board))
