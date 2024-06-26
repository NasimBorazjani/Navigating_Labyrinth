
from collections import deque

def bfs(init_board, target_words):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up-right, down-right, up-left, down-left
    target_state = ''.join(target_words)
    queue = deque([(init_board, '', (0, 0))])  # board, swaps, position of '_'
    visited = set()

    while queue:
        board, swaps, pos = queue.popleft()
        state = ''.join([''.join(row) for row in board])
        if state == target_state:
            return swaps
        if state not in visited:
            visited.add(state)
            for move in moves:
                new_pos = (pos[0] + move[0], pos[1] + move[1])
                if 0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]):
                    new_board = [lst.copy() for lst in board]
                    new_board[pos[0]][pos[1]], new_board[new_pos[0]][new_pos[1]] = new_board[new_pos[0]][new_pos[1]], new_board[pos[0]][pos[1]]
                    queue.append((new_board, swaps + str(move), new_pos))

init_board = [['o', 'g', 'h', 'a'], ['y', 'c', 'd', 'l'], ['o', 'a', '_', 'l'], ['a', 'w', 'l', 'e']]
target_words = ['goa', 'yodh', 'wall', 'acle']
print(bfs(init_board, target_words))
