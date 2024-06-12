
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
    return state[0][1:] == list(target_words[0]) and state[1][:] == list(target_words[1]) and state[2][:] == list(target_words[2]) and state[3][:] == list(target_words[3])

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if is_target_state(state, target_words):
            return path
        for next_state, direction in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                queue.append((next_state, path + [direction]))

    return None

initial_state = [['r', 'p', '_', 'n', 'n', 'o'], ['u', 'o', 'c', 'o', 'i', 'n'], ['l', 'n', 'h', 'i', 'g', 'e'], ['b', 'd', 'i', 'n', 'k', 's']]
target_words = ['pongo', 'urchin', 'ondine', 'blinks']

path = bfs(initial_state, target_words)
print(path)
