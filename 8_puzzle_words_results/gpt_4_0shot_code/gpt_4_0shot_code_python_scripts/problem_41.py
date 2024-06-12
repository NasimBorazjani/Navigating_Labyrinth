
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

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        blank = find_blank(node)
        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
            nx, ny = blank[0] + dx, blank[1] + dy
            if 0 <= nx < len(node) and 0 <= ny < len(node[0]):
                neighbor = swap(node, blank, (nx, ny))
                if "".join(neighbor) not in seen:
                    queue.append((neighbor, path + [(dx, dy)]))
                    seen.add("".join(neighbor))

start = ['oait', 'drooa', 'cemle', 'ccmti']
goal = ['alias', 'doocot', 'cerite', 'commie']
print(bfs(start, goal))
