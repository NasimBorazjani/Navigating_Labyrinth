
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, swaps = queue.popleft()
        if current == target:
            return swaps
        for direction in get_swaps(current):
            new_board, new_swaps = perform_swap(current, direction)
            if new_board not in visited:
                visited.add(new_board)
                queue.append((new_board, swaps + [direction]))

def get_swaps(board):
    swaps = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                if i > 0:
                    swaps.append('U')
                if i < len(board) - 1:
                    swaps.append('D')
                if j > 0:
                    swaps.append('L')
                if j < len(board[0]) - 1:
                    swaps.append('R')
    return swaps

def perform_swap(board, direction):
    new_board = [list(row) for row in board]
    if direction == 'U':
        new_board[1][0], new_board[0][0] = new_board[0][0], new_board[1][0]
    elif direction == 'D':
        new_board[-2][0], new_board[-1][0] = new_board[-1][0], new_board[-2][0]
    elif direction == 'L':
        new_board[0][1], new_board[0][0] = new_board[0][0], new_board[0][1]
    elif direction == 'R':
        new_board[0][-2], new_board[0][-1] = new_board[0][-1], new_board[0][-2]
    return ''.join([''.join(row) for row in new_board]), direction

start = 'uar_hemiimpvavjfimi'
target = 'aerhume_mimpvavfiji'

swaps = bfs(start, target)
print(swaps)
