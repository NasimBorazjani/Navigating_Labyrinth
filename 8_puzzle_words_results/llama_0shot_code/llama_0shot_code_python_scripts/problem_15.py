
from collections import deque

def bfs(initial_board, target_words):
    visited = set()
    queue = deque([(initial_board, [])])
    target_state = ''.join(target_words) + '\n'

    while queue:
        board, swaps = queue.popleft()
        state = ''.join(board) + '\n'

        if state == target_state:
            return swaps

        if state not in visited:
            visited.add(state)

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '_':
                        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < len(board) and 0 <= ny < len(board[i]) and board[nx][ny] != '_':
                                new_board = [row.copy() for row in board]
                                new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                                queue.append((new_board, swaps + [((i, j), (nx, ny))]))

    return None

initial_board = [['a', 'r', '_', 'c'], ['h', 'a', 'v', 'e'], ['a', 'g', 's', 'd'], ['b', 'i', 't', 'z']]
target_words = ['ric', 'have', 'sgad', 'batz']

swaps = bfs(initial_board, target_words)
print(swaps)
