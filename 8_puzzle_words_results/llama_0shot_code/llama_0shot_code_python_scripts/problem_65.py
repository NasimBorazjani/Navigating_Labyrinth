
from collections import deque

def bfs(initial_board, target_words):
    queue = deque([(initial_board, [])])
    target_words = [''.join(word) for word in target_words]
    while queue:
        board, swaps = queue.popleft()
        if target_words == [board[0][1:]] + [board[i][0] + board[i][2:] for i in range(1, len(board))]:
            return swaps
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '_':
                    for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        new_i, new_j = i + di, j + dj
                        if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                            queue.append((new_board, swaps + [f"({i},{j})({new_i},{new_j})"]))

initial_board = [['h', 'n', '_', 'd'], ['w', 'r', 'a', 'e'], ['e', 'o', 'y', 't'], ['h', 'e', 'l', 'm'], ['m', 'i', 'l', 'k']]
target_words = ['ned', 'wham', 'roy', 'hell', 'miek']
print(bfs(initial_board, target_words))
