
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

def bfs(board, target):
    queue = deque([(board, [])])
    seen = set([tuple(board)])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        i, j = find_blank(state)
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                new_state = swap(state, (i, j), (ni, nj))
                if tuple(new_state) not in seen:
                    queue.append((new_state, path + [direction]))
                    seen.add(tuple(new_state))

board = ['uamr', 'heme', 'miip', 'vavj', 'fimi']
target = ['aer', 'hume', 'mimp', 'viva', 'fiji']
print(bfs(board, target))
