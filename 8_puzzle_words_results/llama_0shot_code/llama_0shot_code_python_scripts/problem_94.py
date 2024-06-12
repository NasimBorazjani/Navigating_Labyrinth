
from collections import deque

def generate_next_states(state):
    blank_row, blank_col = None, None
    for r in range(len(state)):
        for c in range(len(state[r])):
            if state[r][c] == '_':
                blank_row, blank_col = r, c
                break
        else:
            continue
        break

    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]  # right, down-right, down, down-left
    next_states = []
    for dr, dc in directions:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[new_row]):
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            next_states.append((tuple(tuple(row) for row in new_state), (dr, dc)))

    return next_states

def is_target_state(state, target_words):
    return state[1:] == [list(word) for word in target_words]

def bfs(initial_state, target_words):
    queue = deque([(initial_state, None)])
    visited = {str(initial_state): None}
    while queue:
        current_state, swaps = queue.popleft()
        if is_target_state(current_state, target_words):
            return swaps
        for next_state, swap in generate_next_states(current_state):
            if str(next_state) not in visited:
                visited[str(next_state)] = swaps + [swap] if swaps else [swap]
                queue.append((next_state, visited[str(next_state)]))

initial_state = [['_', 'd', 'a', 'u', 'n', 'k'], ['a', 'r', 'm', 'r', 'r', 'e'], ['d', 'i', 'u', 'l', 'l', 't'], ['c', 'd', 'u', 'r', 'a', 'c'], ['m', 'i', 'g', 'a', 'o', 'h']]
target_words = ['drunk', 'armure', 'diglot', 'caudal', 'mirach']

swaps = bfs(initial_state, target_words)
print(swaps)
