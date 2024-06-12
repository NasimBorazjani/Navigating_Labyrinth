
from collections import deque

def bfs(board, words):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = deque([(board, [])])
    target = [list(word) for word in words]

    while queue:
        board, move_seq = queue.popleft()
        if board == target:
            return move_seq
        for i, j in moves:
            new_board = [row[:] for row in board]
            new_board[i][j], new_board[0][0] = new_board[0][0], new_board[i][j]
            new_move_seq = move_seq + [(i, j)]
            new_state = (tuple(new_board), new_move_seq)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_board, new_move_seq))

board = [['y', 't', 's', 'n', 'a', 'r'], ['m', 'r', 'r', 't', 'o', 'e'], ['l', 'o', '_', 'd', 'l', 'n'], ['e', 'u', 'v', 'i', 'r', 'a'], ['h', 'e', 'l', 'm', 'a', 'n']]
words = ["tuner", "myrtol", "soldan", "elvira", "herman"]
print(bfs(board, words))
