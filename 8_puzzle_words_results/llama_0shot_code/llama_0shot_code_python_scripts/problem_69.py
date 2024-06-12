
from collections import deque

def bfs(initial_board, words):
    visited = set()
    queue = deque([(initial_board, [])])
    target_state = ''.join(words) + '\n'

    while queue:
        board, swaps = queue.popleft()
        state = ''.join(board) + '\n'

        if state == target_state:
            return swaps

        if state not in visited:
            visited.add(state)

            for i in range(len(board)):
                for j in range(len(board[i])-1):
                    if board[i][j] == '_':
                        new_board = board.copy()
                        new_board[i][j], new_board[i-1][j+1] = new_board[i-1][j+1], new_board[i][j]
                        queue.append((new_board, swaps + [(i, j, i-1, j+1)]))

                        new_board = board.copy()
                        new_board[i][j], new_board[i+1][j+1] = new_board[i+1][j+1], new_board[i][j]
                        queue.append((new_board, swaps + [(i, j, i+1, j+1)]))

                        new_board = board.copy()
                        new_board[i][j], new_board[i-1][j-1] = new_board[i-1][j-1], new_board[i][j]
                        queue.append((new_board, swaps + [(i, j, i-1, j-1)]))

                        new_board = board.copy()
                        new_board[i][j], new_board[i+1][j-1] = new_board[i+1][j-1], new_board[i][j]
                        queue.append((new_board, swaps + [(i, j, i+1, j-1)]))

    return None

initial_board = [['c', 'o', 'a', 'c'], ['i', 'o', 'h', 'r'], ['d', 'e', 'r', 'r'], ['f', 'o', 'u', 'a'], ['p', 'e', '_', 'i']]
words = ['orc', 'icho', 'dear', 'four', 'peai']

swaps = bfs(initial_board, words)
print(swaps)
