
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

def bfs(initial_state, target_words):
    queue = deque([(initial_state, None, [])])
    visited = set()

    while queue:
        state, direction, path = queue.popleft()
        if is_target_state(state, target_words):
            return path if path else ['No swap needed']

        if str(state) not in visited:
            visited.add(str(state))
            next_states = generate_next_states(state)
            for new_state, direction in next_states:
                new_path = path + [direction] if path else [direction]
                queue.append((new_state, direction, new_path))

    return 'No solution'

initial_state = [['e', 'u', 'n', 'a', '_', 'e'], ['d', 'r', 'a', 'v', 'i', 'e'], ['m', 'a', 'n', 'u', 'k', 'a'], ['k', 'h', 'a', 't', 'u', 'm']]
target_words = ['uvate', 'dearie', 'manuka', 'khanum']

print(bfs(initial_state, target_words))
