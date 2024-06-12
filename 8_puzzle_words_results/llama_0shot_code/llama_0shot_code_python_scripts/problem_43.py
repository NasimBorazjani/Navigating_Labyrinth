
from collections import deque

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, words):
    n, m = len(board), len(board[0])
    start = tuple(map(tuple, board))
    target = tuple(map(tuple, [list(word) for word in words]))
    visited = set()
    queue = deque([(start, "")])
    while queue:
        current, direction = queue.popleft()
        if current == target:
            return direction
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        ni, nj = i + dx, j + dy
                        if is_valid(ni, nj, n, m):
                            new_board = [list(row) for row in current]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            new_state = tuple(map(tuple, new_board))
                            new_direction = direction + "urdl"[["up", "right", "down", "left"].index(("up" if dx == -1 else "down") if dy == 1 else ("left" if dx == -1 else "right"))]
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, new_direction))
    return None

words = ["dione", "palmad", "ancona", "saltly"]
board = [['a', 'd', 'a', 'o', 'n', 'e'], ['p', 'm', 'l', 'n', 'a', 'i'], ['_', 'n', 'c', 'o', 'd', 'a'], ['s', 'a', 'l', 't', 'l', 'y']]
print(bfs(board, words))
