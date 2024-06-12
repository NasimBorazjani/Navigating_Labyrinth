
from collections import deque

def bfs(initial_board, target_words):
    # Convert the board into a string for easy comparison
    def board_to_str(board):
        return ''.join([''.join(row) for row in board])

    # Function to get the possible next states (boards)
    def get_next_states(board):
        next_states = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '_':
                    for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]: # The 4 diagonal directions
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(board) and 0 <= nj < len(board[i]):
                            new_board = [list(row) for row in board]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            next_states.append((board_to_str(new_board), (i, j, ni, nj)))
        return next_states

    # The queue for BFS
    queue = deque([(board_to_str(initial_board), [])])

    # The set for visited states
    visited = set()

    while queue:
        current_board, swaps = queue.popleft()
        if current_board == '_' + ''.join(target_words): # The target state is found
            return [swaps[i:i+4] for i in range(0, len(swaps), 4)] # The swaps are grouped by 4
        if current_board not in visited:
            visited.add(current_board)
            for next_board, swap in get_next_states(initial_board):
                queue.append((next_board, swaps + list(swap)))

    return [] # If there is no solution

initial_board = [['_', 'a', 't', 'n'], ['b', 'i', 'r', 'n'], ['k', 'r', 'e', 'y'], ['b', 'a', 'l', 'i']]
target_words = ['ann', 'birk', 'trey', 'bali']
print(bfs(initial_board, target_words))
