
from collections import deque

def generate_next_states(state, path):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(state), len(state[0])
    for i in range(n):
        for j in range(m):
            if state[i][j] == '_':
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        new_state = [row.copy() for row in state]
                        new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
                        new_path = path + [(i, j, nx, ny)]
                        yield (new_state, new_path)

def solve_puzzle(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()
    target_state = [list(word) for word in target_words]
    target_state[0].insert(0, '_')
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == target_state:
            return path
        for next_state in generate_next_states(state, path):
            queue.append(next_state)
    return None

initial_state = [['n', 'j', '_', 'b', 'e', 'y'], ['e', 'i', 't', 'u', 'n', 'o'], ['x', 'e', 'n', 'i', 'b', 'm'], ['e', 'n', 'w', 'o', 'm', 'b']]
target_words = ['jibby', 'entone', 'xenium', 'enwomb']

path = solve_puzzle(initial_state, target_words)
print(path)
