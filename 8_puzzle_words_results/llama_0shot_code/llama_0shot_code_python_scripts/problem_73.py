
from collections import deque

def generate_next_states(state):
    next_states = []
    blank_row, blank_col = None, None
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                blank_row, blank_col = i, j
                break
        else:
            continue
        break

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            next_states.append((new_state, (dr, dc)))

    return next_states

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state not in visited:
            visited.add(str(current_state))
            words = [''.join(row).replace('_', '') for row in current_state]
            if words == target_words:
                return path

            next_states = generate_next_states(current_state)
            for next_state, direction in next_states:
                queue.append((next_state, path + [direction]))

    return None

initial_state = [['o', 't', 'f', 'a', 'g'], ['h', 'r', 'p', 'r', 'd'], ['s', 'h', '_', 'l', 't'], ['n', 'e', 'a', 'e', 'h'], ['f', 'a', 'e', 's', 'e']]
target_words = ['trag', 'hoped', 'shelf', 'neath', 'farse']

path = bfs(initial_state, target_words)
print(path)
