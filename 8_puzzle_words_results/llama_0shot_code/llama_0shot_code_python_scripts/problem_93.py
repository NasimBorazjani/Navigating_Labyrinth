
from collections import deque

def get_neighbors(board):
    n, m = len(board), len(board[0])
    neighbors = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == '_':
                if i > 0:
                    new_board = [row.copy() for row in board]
                    new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
                    neighbors.append(('up', new_board))
                if i < n - 1:
                    new_board = [row.copy() for row in board]
                    new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
                    neighbors.append(('down', new_board))
                if j > 0:
                    new_board = [row.copy() for row in board]
                    new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
                    neighbors.append(('left', new_board))
                if j < m - 1:
                    new_board = [row.copy() for row in board]
                    new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
                    neighbors.append(('right', new_board))
    return neighbors

def is_goal(board, target_words):
    n, m = len(board), len(board[0])
    for i in range(1, n):
        word = ''.join(board[i][j] for j in range(m) if board[i][j] != '_')
        if word != target_words[i - 1]:
            return False
    return True

def bfs(initial_board, target_words):
    queue = deque([(initial_board, [])])
    while queue:
        board, path = queue.popleft()
        if is_goal(board, target_words):
            return path
        for direction, new_board in get_neighbors(board):
            new_path = path + [direction]
            queue.append((new_board, new_path))

initial_board = [['d', 'h', '_', 'l', 'e', 'n'], ['a', 'a', 'e', 'b', 'e', 'u'], ['m', 'u', 'i', 'b', 'e', 'e'], ['i', 'o', 'd', 'm', 's', 'l'], ['t', 'r', 'l', 'l', 'l', 'o']]
target_words = ['helen', 'adelea', 'bumble', 'iodism', 'trullo']

print(bfs(initial_board, target_words))
