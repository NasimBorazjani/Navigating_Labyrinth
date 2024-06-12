
from collections import deque

def sort_the_chars(target, board):
    target = [list(word) for word in target]
    board = [list(row) for row in board]
    actions = ['up-right', 'down-right', 'up-left', 'down-left']
    dx, dy = [-1, 1, -1, 1], [1, 1, -1, -1]
    visited = set()
    queue = deque([((board.index(row), row.index('_')), board, []) for row in board if '_' in row])

    while queue:
        (x, y), state, action_path = queue.popleft()
        if state == target:
            return action_path
        for action, dx, dy in zip(actions, dx, dy):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                new_state = [row.copy() for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                if str(new_state) not in visited:
                    visited.add(str(new_state))
                    queue.append(((nx, ny), new_state, action_path + [action]))

    return "No solution found"

target = ['nieve', 'astely', 'oecist', 'mewler']
board = [['s', 'n', '_', 'e', 'y', 'e'], ['a', 'e', 't', 'i', 'l', 'e'], ['o', 'e', 'c', 'i', 'v', 't'], ['m', 'l', 'w', 's', 'e', 'r']]
print(sort_the_chars(target, board))
