
from collections import deque

def bfs(board, words):
    start = ''.join(map(lambda row: ''.join(row), board))
    goal = ''.join(words) + '_' * len(words)
    visited = set([start])
    queue = deque([(start, [])])
    while queue:
        state, actions = queue.popleft()
        if state == goal:
            return actions
        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_state, new_actions = swap(state, direction)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, actions + [direction]))
    return None

def swap(state, direction):
    board = [list(row) for row in [state[i:i+5] for i in range(0, len(state), 5)]]
    x, y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                x, y = i, j
                break
        else:
            continue
        break
    dx, dy = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}[direction]
    new_x, new_y = x + dx, y + dy
    board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
    new_state = ''.join(map(lambda row: ''.join(row), board))
    return new_state, [direction]

board = [['_', 'm', 'u', 'p'], ['c', 'e', 'r', 'a'], ['d', 'r', 'e', 'b'], ['v', 'e', 'l', 'o']]
words = ['map', 'cere', 'drub', 'velo']
print(bfs(board, words))
