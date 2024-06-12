
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

    return []

def swap(state, path, direction):
    new_state = [list(row) for row in state]
    i, j = find_blank(state)

    if direction == 'up-right' and i > 0 and j < len(state[0]) - 1:
        new_state[i][j], new_state[i - 1][j + 1] = new_state[i - 1][j + 1], new_state[i][j]
    elif direction == 'down-right' and i < len(state) - 1 and j < len(state[0]) - 1:
        new_state[i][j], new_state[i + 1][j + 1] = new_state[i + 1][j + 1], new_state[i][j]
    elif direction == 'up-left' and i > 0 and j > 0:
        new_state[i][j], new_state[i - 1][j - 1] = new_state[i - 1][j - 1], new_state[i][j]
    elif direction == 'down-left' and i < len(state) - 1 and j > 0:
        new_state[i][j], new_state[i + 1][j - 1] = new_state[i + 1][j - 1], new_state[i][j]

    return new_state, path + [direction]

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

initial_board = [['a', 's', 'i', 'u', 'r'], ['m', 'z', 'n', 'k', 'y'], ['g', 'i', 'o', 'i', 'l'], ['l', 'o', 'g', 'i', 'a'], ['u', 'r', '_', 'a', 'n']]
target_board = [['_', 's', 'o', 'u', 'r'], ['m', 'a', 'n', 'g', 'y'], ['k', 'i', 'z', 'i', 'l'], ['l', 'o', 'g', 'i', 'a'], ['u', 'r', 'i', 'a', 'n']]

print(bfs(initial_board, target_board))
