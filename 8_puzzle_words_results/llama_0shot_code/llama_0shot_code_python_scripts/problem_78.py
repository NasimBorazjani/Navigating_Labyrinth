
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
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[new_row]):
            new_state = [list(row) for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            next_states.append((new_state, direction))

    return next_states

def shortest_path(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()

    target_state = [list(word) for word in target_words]
    for i in range(len(target_state)):
        target_state[i].insert(0, '_')

    while queue:
        current_state, actions = queue.popleft()
        if current_state not in visited:
            visited.add(tuple(map(tuple, current_state)))
            if current_state == target_state:
                return actions
            next_states = generate_next_states(current_state)
            for next_state, action in next_states:
                queue.append((next_state, actions + [action]))

    return []

initial_state = [['a', 'j', '_', 'k', 'e'], ['t', 's', 'w', 'y', 'e'], ['t', 'r', 'a', 'p', 'a'], ['s', 'e', 'a', 'm', 'h'], ['c', 'r', 's', 'e', 'p']]
target_words = ['jake', 'tawse', 'trypa', 'smash', 'creep']

print(shortest_path(initial_state, target_words))
