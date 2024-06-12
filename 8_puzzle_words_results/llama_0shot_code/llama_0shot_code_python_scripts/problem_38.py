
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
        nr, nc = blank_row + dr, blank_col + dc
        if 0 <= nr < len(state) and 0 <= nc < len(state[nr]):
            new_state = [row.copy() for row in state]
            new_state[blank_row][blank_col], new_state[nr][nc] = new_state[nr][nc], new_state[blank_row][blank_col]
            next_states.append((new_state, (dr, dc)))

    return next_states

def is_target_state(state, target_words):
    return state[1:] == [list(word) for word in target_words]

def shortest_path_to_target(initial_state, target_words):
    queue = deque([(initial_state, None, [])])
    visited = {str(initial_state): None}

    while queue:
        state, direction, path = queue.popleft()
        if is_target_state(state, target_words):
            return path

        for next_state, direction in generate_next_states(state):
            if str(next_state) not in visited:
                visited[str(next_state)] = direction
                queue.append((next_state, direction, path + [direction]))

    return None

initial_state = [['s', 'n', '_', 'e', 'y', 'e'], ['a', 'e', 't', 'i', 'l', 'e'], ['o', 'e', 'c', 'i', 'v', 't'], ['m', 'l', 'w', 's', 'e', 'r']]
target_words = ["nieve", "astely", "oecist", "mewler"]

path = shortest_path_to_target(initial_state, target_words)
print(path)
