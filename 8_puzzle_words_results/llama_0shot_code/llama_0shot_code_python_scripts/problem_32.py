
from collections import deque

def generate_next_states(state, path):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = state.index('_'), state.index('_', 1)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state):
            new_state = list(state)
            new_state[nx], new_state[y] = new_state[y], new_state[nx]
            new_path = path + [dx, dy]
            yield ''.join(new_state), new_path

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()
    target_state = ['_'] + list(''.join(target_words))
    while queue:
        state, path = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state == target_state:
                return path
            for next_state, next_path in generate_next_states(state, path):
                queue.append((next_state, next_path))

initial_state = [['o', 'f', '_', 'c', 'k'], ['s', 'n', 'f', 's', 'a'], ['o', 'i', 'i', 's', 'e'], ['n', 'e', 's', 'a', 'y']]
target_words = ['fack', 'sofia', 'nisse', 'nosey']

path = bfs(initial_state, target_words)
print(path)
