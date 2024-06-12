
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]
    return board

def generate_states(board, i, j):
    states = []
    directions = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for di, dj in directions:
        if 0 <= di < len(board) and 0 <= dj < len(board[0]):
            new_board = [row[:] for row in board]
            states.append(swap(new_board, i, j, di, dj))
    return states

def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = set([str(initial)])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        i, j = find_blank(state)
        for new_state in generate_states(state, i, j):
            str_state = str(new_state)
            if str_state not in visited:
                queue.append((new_state, path + [(i, j)]))
                visited.add(str_state)

initial = [['u', 'k', 'd', 'x'], ['t', 'e', 'r', 'b'], ['w', 'a', '_', 'i'], ['t', 'e', 's', 't']]
goal = [['_', 'k', 'e', 'x'], ['t', 'u', 'r', 'd'], ['w', 'a', 'b', 'i'], ['t', 'e', 's', 't']]
print(bfs(initial, goal))
