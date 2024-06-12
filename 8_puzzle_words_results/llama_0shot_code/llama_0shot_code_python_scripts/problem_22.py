
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
            for next_state, new_path in generate_next_states(state, path):
                queue.append((next_state, new_path))

initial_state = [['o', 'j', '_', 'h', 'u'], ['w', 'l', 'r', 'e', 'y'], ['n', 'i', 'l', 't', 'a'], ['i', 'y', 'i', 'm', 'l']]
target_words = ['jehu', 'wormy', 'linty', 'ilial']

path = bfs(initial_state, target_words)
print(path)
