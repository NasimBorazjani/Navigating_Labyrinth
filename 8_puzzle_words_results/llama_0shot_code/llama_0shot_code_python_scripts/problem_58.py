
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

def sort_board(initial_state, target_words):
    queue = deque([(initial_state, None)])
    visited = set()
    while queue:
        state, direction = queue.popleft()
        if direction is not None:
            yield direction
        state_str = str(state)
        if state_str in visited:
            continue
        visited.add(state_str)
        if is_target_state(state, target_words):
            return
        for next_state, direction in generate_next_states(state):
            queue.append((next_state, direction))

initial_state = [['i', 'e', 'e', 'd'], ['v', 't', 'n', 'l'], ['o', 'd', '_', 'a'], ['p', 'r', 'c', 'e'], ['p', 'i', 'o', 'l']]
target_words = ['eld', 'vint', 'edea', 'poco', 'pirl']

print(list(sort_board(initial_state, target_words)))
