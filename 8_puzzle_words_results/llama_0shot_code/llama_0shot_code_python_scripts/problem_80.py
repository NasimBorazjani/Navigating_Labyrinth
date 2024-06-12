
from collections import deque

def generate_next_states(state):
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
    next_states = []
    for direction in directions:
        new_row, new_col = blank_row + direction[0], blank_col + direction[1]
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            next_states.append((new_state, direction))

    return next_states

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, swap_actions = queue.popleft()
        current_words = [''.join(row) for row in current_state]
        if current_words == target_words:
            return swap_actions
        if str(current_state) not in visited:
            visited.add(str(current_state))
            next_states = generate_next_states(current_state)
            for next_state, direction in next_states:
                new_swap_actions = swap_actions + [direction]
                queue.append((next_state, new_swap_actions))

    return None

initial_state = [['d', 'w', 'p', 'l', 't'], ['e', 'i', 'd', 'e', 'c'], ['_', 'q', 'e', 'i', 'r'], ['m', 'e', 'c', 'u', 'r'], ['y', 'u', 'a', 't', 'a']]
target_words = ['welt', 'eddic', 'equip', 'macer', 'yurta']

result = bfs(initial_state, target_words)
print(result)
