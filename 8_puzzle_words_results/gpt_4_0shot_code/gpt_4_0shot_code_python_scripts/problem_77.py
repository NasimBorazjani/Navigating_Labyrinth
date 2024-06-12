
from collections import deque

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path

        for direction in ['up-right', 'down-right', 'up-left', 'down-left']:
            new_state, new_path = swap(state, path, direction)
            if new_state not in visited:
                queue.append((new_state, new_path))
                visited.add(new_state)

def swap(state, path, direction):
    new_state = [list(row) for row in state]
    i, j = find_blank(state)
    if direction == 'up-right' and i > 0 and j < len(state[0]) - 1:
        new_state[i][j], new_state[i-1][j+1] = new_state[i-1][j+1], new_state[i][j]
    elif direction == 'down-right' and i < len(state) - 1 and j < len(state[0]) - 1:
        new_state[i][j], new_state[i+1][j+1] = new_state[i+1][j+1], new_state[i][j]
    elif direction == 'up-left' and i > 0 and j > 0:
        new_state[i][j], new_state[i-1][j-1] = new_state[i-1][j-1], new_state[i][j]
    elif direction == 'down-left' and i < len(state) - 1 and j > 0:
        new_state[i][j], new_state[i+1][j-1] = new_state[i+1][j-1], new_state[i][j]
    else:
        return state, path
    return new_state, path + [direction]

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '_':
                return i, j

initial_board = [['l', 'g', 'a', 'n', 'g'], ['c', 'o', 'o', 'e', 'n'], ['e', 'r', '_', 'n', 't'], ['d', 'b', 'w', 'o', 'x'], ['t', 'h', 'w', 'r', 'p']]
target_board = [['_', 'g', 'o', 'n', 'g'], ['c', 'l', 'o', 'w', 'n'], ['b', 'r', 'e', 'n', 't'], ['d', 'e', 'w', 'a', 'x'], ['t', 'h', 'o', 'r', 'p']]
print(bfs(initial_board, target_board))
