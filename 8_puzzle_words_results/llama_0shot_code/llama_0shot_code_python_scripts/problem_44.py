
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
        if 0 <= nr < len(state) and 0 <= nc < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[blank_row][blank_col], new_state[nr][nc] = new_state[nr][nc], new_state[blank_row][blank_col]
            next_states.append(new_state)

    return next_states

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, actions = queue.popleft()
        if tuple(map(tuple, current_state)) in visited:
            continue
        visited.add(tuple(map(tuple, current_state)))

        words = [current_state[i][1:] for i in range(1, len(current_state))]
        if words == target_words:
            return actions

        next_states = generate_next_states(current_state)
        for next_state, direction in zip(next_states, ['ur', 'ul', 'dr', 'dl']):
            queue.append((next_state, actions + [direction]))

    return None

initial_state = [['h', 'b', 'n', 's', 'i', 't'], ['t', 'e', 'r', 'k', 'v', 'e'], ['i', 'i', '_', 'c', 'o', 'b'], ['h', 'u', 'm', 'a', 't', 'e']]
target_words = ['besit', 'thrive', 'kincob', 'humate']

print(bfs(initial_state, target_words))
