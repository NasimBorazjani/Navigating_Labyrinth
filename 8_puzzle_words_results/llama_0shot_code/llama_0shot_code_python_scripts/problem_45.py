
from collections import deque

def bfs(board, words):
    start = (board, None)
    queue = deque([(start, [])])
    visited = set()
    moves = [(0, 1), (1, 1), (1, 0), (1, -1)]  # up-right, down-right, up-left, down-left

    while queue:
        (current_board, direction), actions = queue.popleft()
        current_board_str = ''.join([''.join(row) for row in current_board])
        if current_board_str == ''.join(words):
            return actions
        if (current_board, direction) not in visited:
            visited.add((current_board, direction))
            for i in range(len(current_board)):
                for j in range(len(current_board[i])):
                    if current_board[i][j] == '_':
                        for move in moves:
                            new_i, new_j = i + move[0], j + move[1]
                            if 0 <= new_i < len(current_board) and 0 <= new_j < len(current_board[i]):
                                new_board = [list(row) for row in current_board]
                                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                                queue.append(((new_board, (new_i - i, new_j - j)), actions + [(i, j, new_i, new_j)]))
    return None

words = ['khadi', 'swarmy', 'aguish', 'wheaty']
board = [['w', 'k', 'u', 'a', 'd', 'i'], ['s', 'a', 'a', 'r', 'm', 'y'], ['h', 'g', '_', 'i', 's', 'h'], ['w', 'h', 'e', 'a', 't', 'y']]

print(bfs(board, words))
