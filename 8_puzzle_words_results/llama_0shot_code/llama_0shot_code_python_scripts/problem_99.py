
from collections import deque

def generate_next_states(state, blank_row, blank_col):
    next_states = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_blank_row, new_blank_col = blank_row + direction[0], blank_col + direction[1]
        if 0 <= new_blank_row < len(state) and 0 <= new_blank_col < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[blank_row][blank_col], new_state[new_blank_row][new_blank_col] = new_state[new_blank_row][new_blank_col], new_state[blank_row][blank_col]
            next_states.append((new_state, direction))
    return next_states

def is_target_state(state, target_words):
    return state[1:] == [list(word) for word in target_words]

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [], 0)])
    visited = set()
    while queue:
        current_state, path, swaps = queue.popleft()
        if is_target_state(current_state, target_words):
            return path
        blank_row, blank_col = 0, 0
        for row in current_state:
            if '_' in row:
                blank_row = current_state.index(row)
                blank_col = row.index('_')
                break
        for next_state, direction in generate_next_states(current_state, blank_row, blank_col):
            if tuple(next_state[1:]) not in visited:
                visited.add(tuple(next_state[1:]))
                queue.append((next_state, path + [direction], swaps + 1))

initial_state = [['_', 'c', 'a', 'a', 'n', 'k'], ['h', 'm', 'r', 'l', 'i', 'g'], ['h', 'i', 'o', 't', 'u', 'g'], ['t', 'n', 'r', 't', 'a', 'c'], ['z', 'y', 't', 'h', 'm']]
target_words = ['chank', 'hormic', 'tigtag', 'tornal', 'zythum']

print(bfs(initial_state, target_words))
