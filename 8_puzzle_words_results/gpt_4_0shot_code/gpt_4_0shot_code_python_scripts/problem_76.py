
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

def get_neighbors(pos):
    x, y = pos
    neighbors = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    return [(i, j) for i, j in neighbors if 0 <= i < 5 and 0 <= j < 5]

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([tuple(start)])
    while queue:
        board, path = queue.popleft()
        if board == target:
            return path
        blank = find_blank(board)
        for neighbor in get_neighbors(blank):
            new_board = swap(board, blank, neighbor)
            if tuple(new_board) not in seen:
                queue.append((new_board, path + [neighbor]))
                seen.add(tuple(new_board))

start = ['hqnag', 'byado', 'decao', 'honur', 'picky']
target = ['quad_', 'bhang', 'decay', 'honor', 'picky']
print(bfs(start, target))
