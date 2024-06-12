
from collections import deque

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return i, j

def valid_actions(i, j, n, m):
    actions = []
    if i > 0 and j < m - 1:
        actions.append(('up-right', (i - 1, j + 1)))
    if i < n - 1 and j < m - 1:
        actions.append(('down-right', (i + 1, j + 1)))
    if i > 0 and j > 0:
        actions.append(('up-left', (i - 1, j - 1)))
    if i < n - 1 and j > 0:
        actions.append(('down-left', (i + 1, j - 1)))
    return actions

def swap(board, pos1, pos2):
    board = [list(row) for row in board]
    board[pos1[0]][pos1[1]], board[pos2[0]][pos2[1]] = board[pos2[0]][pos2[1]], board[pos1[0]][pos1[1]]
    return [tuple(row) for row in board]

def sort_the_chars(board, target):
    n, m = len(board), len(board[0])
    target = [tuple(word) for word in target]
    queue = deque([(board, [])])
    visited = set([board])
    while queue:
        state, actions = queue.popleft()
        if state == target:
            return actions
        i, j = find_blank(state)
        for action, pos in valid_actions(i, j, n, m):
            new_state = swap(state, (i, j), pos)
            if new_state not in visited:
                queue.append((new_state, actions + [action]))
                visited.add(new_state)
    return None

initial_board = [('h', 'k', 't', 'n'), ('k', 'e', 'a', 'k'), ('e', 'i', '_', 'l'), ('w', 'l', 'n', 't')]
target_words = ['ken', 'khat', 'kill', 'went']
print(sort_the_chars(initial_board, target_words))
