
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def is_goal(board, target):
    return [''.join(row) for row in board] == target

def neighbors(board, i, j):
    for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
        if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
            swap(board, i, j, i + di, j + dj)
            yield list(map(list, board)), (di, dj)
            swap(board, i, j, i + di, j + dj)

def solve(board, target):
    start = list(map(list, board))
    queue = deque([(start, [])])
    seen = {str(start)}
    while queue:
        board, path = queue.popleft()
        if is_goal(board, target):
            return path
        i, j = find_blank(board)
        for next_board, direction in neighbors(board, i, j):
            if str(next_board) not in seen:
                queue.append((next_board, path + [direction]))
                seen.add(str(next_board))

board = [['a', 'n', 'x', 'e'], ['c', 'y', 'l', 'a'], ['r', 'e', '_', 'n'], ['j', 'h', 'o', 'a'], ['e', 'x', 'b', 'm']]
target = ['nye', 'calx', 'hern', 'jaob', 'exam']
print(solve(board, target))
