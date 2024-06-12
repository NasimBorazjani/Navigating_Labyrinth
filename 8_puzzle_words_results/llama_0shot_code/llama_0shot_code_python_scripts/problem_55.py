
from collections import deque

def generate_next_states(state, x, y):
    next_states = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state[0]) and state[nx][ny] != '_':
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            next_states.append((new_state, nx, ny))
    return next_states

def solve_puzzle(initial_state, target_words):
    queue = deque([(initial_state, 0, 0, [])])
    visited = set()
    target_words = set(target_words)
    while queue:
        state, x, y, swaps = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        rows = [''.join(row) for row in state]
        if set(rows[1:]) == target_words:
            return swaps
        next_states = generate_next_states(state, x, y)
        for next_state, nx, ny in next_states:
            queue.append((next_state, nx, ny, swaps + [(nx - x, ny - y)]))
    return None

initial_state = [['o', 'n', 's', 't'], ['t', 'e', 's', 'w'], ['i', 'l', 's', 'p'], ['s', 'g', 'a', 'f'], ['b', 'o', '_', 'n']]
target_words = ['net', 'toss', 'flip', 'swag', 'bosn']

swaps = solve_puzzle(initial_state, target_words)
print(swaps)
