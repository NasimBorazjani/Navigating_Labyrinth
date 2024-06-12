
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
    queue = deque([(initial_state, None)])
    visited = set()

    while queue:
        state, direction = queue.popleft()
        if is_target_state(state, target_words):
            actions = []
            while direction is not None:
                actions.append(direction)
                state, direction = queue.popleft()
            return actions[::-1]

        for next_state, direction in generate_next_states(state):
            if tuple(map(tuple, next_state)) not in visited:
                visited.add(tuple(map(tuple, next_state)))
                queue.append((next_state, direction))

    return None

initial_state = [['l', 'a', 'e', 'o', 'n'], ['p', 'z', 'i', 'n', 'r'], ['l', 'a', 'g', 'o', '_'], ['i', 'e', 'e', 'u', 'm']]
target_words = ["aeon", "plier", "gazon", "ileum"]

print(shortest_path_to_target(initial_state, target_words))
