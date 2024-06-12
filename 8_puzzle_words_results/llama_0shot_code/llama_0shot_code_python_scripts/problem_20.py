
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

    for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            next_states.append((new_state, dr, dc))

    return next_states

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, swaps = queue.popleft()
        current_words = [''.join(row) for row in current_state]

        if current_words == target_words:
            return swaps

        if str(current_state) not in visited:
            visited.add(str(current_state))

            next_states = generate_next_states(current_state)
            for new_state, dr, dc in next_states:
                new_swaps = swaps + [dr, dc]
                queue.append((new_state, new_swaps))

    return None

initial_state = [['r', 's', 'w', 'o', 'g'], ['t', 'n', 'e', 'm', 'a'], ['m', 'o', '_', 'u', 's'], ['a', 'w', 'i', 'r', 'i']]
target_words = ['snog', 'trema', 'mosur', 'awiwi']

swaps = bfs(initial_state, target_words)
print(swaps)
