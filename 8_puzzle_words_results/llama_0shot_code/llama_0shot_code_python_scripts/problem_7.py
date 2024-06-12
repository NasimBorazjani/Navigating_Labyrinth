
from collections import deque

def bfs(init_board, target_words):
    moves = [(0, 1), (1, 1), (1, 0), (1, -1)]  # up-right, down-right, up-left, down-left
    target_state = ''.join(target_words)
    queue = deque([(init_board, [])])
    visited = set()

    while queue:
        board, swaps = queue.popleft()
        state = ''.join([''.join(row) for row in board])

        if state == target_state:
            return swaps

        if state not in visited:
            visited.add(state)

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '_':
                        for move in moves:
                            ni, nj = i + move[0], j + move[1]
                            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                                new_board = [lst[:] for lst in board]
                                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                                queue.append((new_board, swaps + [move]))

    return None

init_board = [['u', 'c', 'r', 'y'], ['d', 'n', 'n', 'r'], ['_', 'u', 'm', 'p'], ['k', 'e', 'e', 'e']]
target_words = ['cry', 'dune', 'rump', 'knee']

swaps = bfs(init_board, target_words)
print(swaps)
