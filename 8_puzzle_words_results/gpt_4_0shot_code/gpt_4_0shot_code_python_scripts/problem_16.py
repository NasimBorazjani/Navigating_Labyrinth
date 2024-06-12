
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def swap(board, pos1, pos2):
    board = [list(row) for row in board]
    board[pos1[0]][pos1[1]], board[pos2[0]][pos2[1]] = board[pos2[0]][pos2[1]], board[pos1[0]][pos1[1]]
    return ["".join(row) for row in board]

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([tuple(start)])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank = find_blank(state)
        for dx, dy, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            nx, ny = blank[0] + dx, blank[1] + dy
            if 0 <= nx < len(state) and 0 <= ny < len(state[0]):
                new_state = swap(state, blank, (nx, ny))
                if tuple(new_state) not in seen:
                    queue.append((new_state, path + [direction]))
                    seen.add(tuple(new_state))

start = ['ogh', 'ycdl', 'oa_l', 'awle']
target = ['goa', 'yodh', 'wall', 'acle']
print(bfs(start, target))
