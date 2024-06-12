
from collections import deque

def bfs(board):
    target_words = ['sour', 'mangy', 'kizil', 'logia', 'urian']
    target_board = [list(word) for word in target_words]
    target_board.insert(0, ['_'] + target_board[0])
    visited = set()
    queue = deque([((board,), '')])
    while queue:
        moves, direction = queue.popleft()
        board = moves[-1]
        if board == target_board:
            return direction
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[nx]) and board[nx][ny] != '_':
                            new_board = [row.copy() for row in board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_moves = moves + (new_board,)
                            new_direction = direction + 'urdl'[['up', 'right', 'down', 'left'].index((dx, dy))]
                            if new_moves not in visited:
                                visited.add(new_moves)
                                queue.append((new_moves, new_direction))
    return None

initial_board = [['a', 's', 'i', 'u', 'r'], ['m', 'z', 'n', 'k', 'y'], ['g', 'i', 'o', 'i', 'l'], ['l', 'o', 'g', 'i', 'a'], ['u', 'r', '_', 'a', 'n']]
print(bfs(initial_board))
