
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return i, j

def swap(board, i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def generate_states(board, i, j):
    states = []
    directions = [(i-1, j+1), (i+1, j+1), (i-1, j-1), (i+1, j-1)]
    for di, dj in directions:
        if 0 <= di < len(board) and 0 <= dj < len(board[di]):
            new_board = [row[:] for row in board]
            swap(new_board, i, j, di, dj)
            states.append(new_board)
    return states

def bfs(initial, goal):
    queue = deque([(initial, [])])
    seen = set([str(initial)])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        i, j = find_blank(state)
        for new_state in generate_states(state, i, j):
            if str(new_state) not in seen:
                queue.append((new_state, path + [(i, j)]))
                seen.add(str(new_state))

initial = [['a', 'd', 'a', 'o', 'n', 'e'], ['p', 'm', 'l', 'n', 'a', 'i'], ['_', 'n', 'c', 'o', 'd', 'a'], ['s', 'a', 'l', 't', 'l', 'y']]
goal = [['_', 'd', 'i', 'o', 'n', 'e'], ['p', 'a', 'l', 'm', 'a', 'd'], ['a', 'n', 'c', 'o', 'n', 'a'], ['s', 'a', 'l', 't', 'l', 'y']]
print(bfs(initial, goal))
