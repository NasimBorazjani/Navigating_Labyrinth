
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target):
    n, m = len(board), len(board[0])
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    dir = ['up-left', 'down-left', 'up-right', 'down-right']
    visited = set()
    queue = deque([(board, [], find_blank(board))])
    while queue:
        curr_board, actions, (x, y) = queue.popleft()
        if curr_board == target:
            return actions
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny, n, m):
                new_board = [row[:] for row in curr_board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                new_state = (tuple(tuple(row) for row in new_board), actions + [dir[i]], (nx, ny))
                if new_state not in visited:
                    queue.append(new_state)
                    visited.add(new_state)
    return []

initial_board = [['a', 'l', '_', 't', 'e'], ['s', 'h', 'r', 'b', 's'], ['e', 'r', 'u', 'a', 'n'], ['w', 'y', 'i', 'n', 'g']]
target_words = [['l', 'e', 't', 'e'], ['s', 'a', 'r', 'u', 's'], ['b', 'r', 'y', 'a', 'n'], ['w', 'h', 'i', 'n', 'g']]
print(bfs(initial_board, target_words))
