
from collections import deque

def generate_next_states(state, path):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(state), len(state[0])
    for i in range(n):
        for j in range(m):
            if state[i][j] == '_':
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < n and 0 <= nj < m:
                        new_state = [row.copy() for row in state]
                        new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                        new_path = path + [d]
                        yield (new_state, new_path)

def solve_puzzle(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()
    target_words = set(target_words)
    while queue:
        state, path = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        if state[1:] == target_words:
            return path
        queue.extend(generate_next_states(state, path))
    return None

initial_state = [['a', 'n', '_', 'l', 'l', 'e'], ['y', 'p', 'p', 'o', 'a', 'n'], ['r', 'i', 'm', 'a', 'y', 'a'], ['c', 't', 'a', 'w', 'l', 'y']]
target_words = ['nolle', 'yapman', 'pitaya', 'crawly']

print(solve_puzzle(initial_state, target_words))
