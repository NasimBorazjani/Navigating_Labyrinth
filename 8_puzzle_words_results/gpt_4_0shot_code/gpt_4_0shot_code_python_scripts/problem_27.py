
from collections import deque

def bfs(target, start):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, action in neighbors(state):
            if next_state not in visited:
                queue.append((next_state, path + [action]))
                visited.add(next_state)
    return None

def neighbors(state):
    i, j = next((i, j) for i in range(len(state)) for j in range(len(state[0])) if state[i][j] == '_')
    for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(state) and 0 <= nj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[ni][nj] = next_state[ni][nj], next_state[i][j]
            yield next_state, action

target = [['b', 'o', 'i', 's', '_'], ['d', 'u', 'r', 'o', 'c'], ['l', 'i', 'n', 'e', 'n'], ['s', 'p', 'e', 'n', 't']]
start = [['_', 'b', 'p', 'i', 's'], ['d', 'u', 'r', 'n', 'c'], ['l', 'i', 'o', 'e', 'n'], ['s', 'n', 'e', 'o', 't']]
print(bfs(target, start))
