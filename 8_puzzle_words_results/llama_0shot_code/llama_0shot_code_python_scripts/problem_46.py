
from collections import deque

def generate_next_states(state, path):
    n, m = len(state), len(state[0])
    for i in range(n):
        for j in range(m):
            if state[i][j] == '_':
                for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        new_state = [row.copy() for row in state]
                        new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
                        new_path = path + [(i, j, nx, ny)]
                        yield (tuple(map(tuple, new_state)), new_path)

def solve_puzzle(start_state, target_words):
    start_state = tuple(map(tuple, start_state))
    target_state = tuple(word for word in target_words)
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == target_state:
            return path
        if state not in visited:
            visited.add(state)
            for next_state, next_path in generate_next_states(state, path):
                queue.append((next_state, next_path))

initial_state = [['e', 'a', 'y', 'u', 'i', 'e'], ['m', 'k', 's', 'o', 'd', 'l'], ['c', 'a', '_', 'l', 'e', 'd'], ['g', 'l', 'r', 'o', 'u', 's']]
target_words = ['akule', 'mesode', 'callid', 'gyrous']

path = solve_puzzle(initial_state, target_words)
print(path)
