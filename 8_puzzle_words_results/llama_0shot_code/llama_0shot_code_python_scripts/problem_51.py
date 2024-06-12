
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

def is_target_state(state, target_words):
    return state[2][:-1] == target_words

def bfs(initial_state, target_words):
    queue = deque([(initial_state, None)])
    while queue:
        state, direction = queue.popleft()
        if is_target_state(state, target_words):
            actions = []
            while direction is not None:
                actions.append(direction)
                state, direction = queue.popleft()
            return actions[::-1]
        next_states = generate_next_states(state)
        for next_state, direction in next_states:
            queue.append((next_state, direction))
    return None

initial_state = [['l', 'b', 'l', 'u', 'i', 'e'], ['a', 't', 'g', 'n', 's', 'c'], ['l', 'a', 'o', 'u', '_', 'e'], ['n', 'i', 'n', 'p', 'o', 'n']]
target_words = ['biune', 'algist', 'palule', 'noncon']

actions = bfs(initial_state, target_words)
print(actions)
