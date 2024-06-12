
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
    queue = deque([(initial_state, None)])
    while queue:
        state, direction = queue.popleft()
        if is_target_state(state, target_words):
            return direction
        next_states = generate_next_states(state)
        for new_state, direction in next_states:
            queue.append((new_state, direction))
    return None

initial_state = [['l', 'a', 'd', 'd', 'e', 'd'], ['a', 'h', 't', 'g', 'e', 'a'], ['_', 'n', 'd', 'i', 'r', 'n'], ['p', 'a', 't', 'i', 'o', 'n']]
target_words = ['added', 'althea', 'indign', 'patron']

directions = []
direction = bfs(initial_state, target_words)
while direction is not None:
    directions.append(direction)
    direction = bfs(initial_state, target_words)

print(directions[::-1])
