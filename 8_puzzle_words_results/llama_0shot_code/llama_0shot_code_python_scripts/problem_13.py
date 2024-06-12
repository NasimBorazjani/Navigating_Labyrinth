
from collections import deque

def bfs(board, words):
    initial_board = ''.join([''.join(row) for row in board])
    queue = deque([(initial_board, '')])
    visited = set()
    while queue:
        current_board, actions = queue.popleft()
        if current_board == ''.join(words):
            return actions
        for i in range(len(current_board)):
            for j in [1, -1, len(current_board), -len(current_board)]:
                if 0 <= i + j < len(current_board) and current_board[i] == '_' and current_board[i + j] != '_':
                    new_board = list(current_board)
                    new_board[i], new_board[i + j] = new_board[i + j], new_board[i]
                    new_board = ''.join(new_board)
                    new_actions = actions + ('u' if j == -1 else 'd' if j == 1 else 'l' if j == len(current_board) else 'r')
                    if new_board not in visited:
                        visited.add(new_board)
                        queue.append((new_board, new_actions))

words = ['lag', 'abas', 'numa', 'sham']
board = [['b', 'l', '_', 'g'], ['a', 'n', 'a', 's'], ['m', 'u', 'a', 'a'], ['s', 'h', 'a', 'm']]
print(bfs(board, words))
