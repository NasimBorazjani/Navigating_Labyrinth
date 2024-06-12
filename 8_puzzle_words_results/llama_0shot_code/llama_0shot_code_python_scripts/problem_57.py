
from collections import deque

def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < len(state) and 0 <= new_y < len(state[i]):
                        new_state = [list(row) for row in state]
                        new_state[i][j], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[i][j]
                        next_states.append((new_state, (dx, dy)))
    return next_states

def is_final_state(state, target_words):
    return state[1:] == [list(word) for word in target_words]

def shortest_path(initial_state, target_words):
    queue = deque([(initial_state, None, [])])
    visited = set()
    while queue:
        state, direction, path = queue.popleft()
        if is_final_state(state, target_words):
            return path
        for next_state, direction in generate_next_states(state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                queue.append((next_state, direction, path + [direction] if direction else path))

initial_state = [['u', 't', '_', 'e'], ['k', 'a', 'b', 'm'], ['n', 'e', 'o', 'g'], ['p', 'u', 's', 'o'], ['y', 'o', 'e', 'p']]
target_words = ['toe', 'kuba', 'meng', 'peso', 'youp']

print(shortest_path(initial_state, target_words))
