
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(board, target):
    n, m = len(board), len(board[0])
    start = find_blank(board)
    queue = deque([(board, start, [])])
    visited = set()

    while queue:
        state, blank, actions = queue.popleft()
        if state == target:
            return actions

        for dx, dy, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            x, y = blank[0] + dx, blank[1] + dy
            if is_valid(x, y, n, m):
                new_state = [row[:] for row in state]
                new_state[blank[0]][blank[1]], new_state[x][y] = new_state[x][y], new_state[blank[0]][blank[1]]
                if str(new_state) not in visited:
                    queue.append((new_state, (x, y), actions + [action]))
                    visited.add(str(new_state))

    return []

target = [['s', 'i', 'v', 'a', '_'], ['b', 'r', 'y', 'c', 'e'], ['b', 'i', 'r', 'n', 'y'], ['p', 'u', 'g', 'i', 'l'], ['l', 'i', 'n', 'n', 'e']]
board = [['r', 's', 'c', 'v', 'a'], ['b', 'b', 'y', 'r', 'e'], ['u', 'i', '_', 'n', 'i'], ['p', 'n', 'g', 'i', 'l'], ['l', 'i', 'y', 'n', 'e']]

print(bfs(board, target))
