
from collections import deque

def generate_next_states(state, x, y):
    next_states = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state[0]) and state[nx][ny] != '_':
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            next_states.append((new_state, nx, ny))
    return next_states

def bfs(initial_state, target_words):
    queue = deque([(initial_state, 0, 0, [])])
    visited = set()
    while queue:
        state, x, y, swaps = queue.popleft()
        if state not in visited:
            visited.add(state)
            words = [state[i][1:] for i in range(1, len(state))]
            words.insert(0, state[0][1:])
            if words == target_words:
                return swaps
            next_states = generate_next_states(state, x, y)
            for next_state, nx, ny in next_states:
                nswaps = swaps + [(nx - x, ny - y)]
                queue.append((next_state, nx, ny, nswaps))
    return None

initial_state = [['_', 'c', 'a', 'r', 'd'], ['s', 'u', 'l', 'c', 'a'], ['v', 'h', 'y', 'n', 'o'], ['s', 'e', 'l', 's', 'm'], ['b', 'i', 'u', 'h', 'y']]
target_words = ['card', 'sylva', 'shune', 'solum', 'bichy']

swaps = bfs(initial_state, target_words)
print(swaps)
