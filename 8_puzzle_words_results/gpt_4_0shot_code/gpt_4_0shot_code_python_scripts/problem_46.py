
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, action in get_neighbors(state):
            if next_state not in visited:
                queue.append((next_state, path + [action]))
                visited.add(next_state)
    return None

def get_neighbors(state):
    i, j = find_blank(state)
    neighbors = []
    if i > 0 and j < len(state[0]) - 1:
        neighbors.append(swap(state, i, j, i - 1, j + 1, 'up-right'))
    if i < len(state) - 1 and j < len(state[0]) - 1:
        neighbors.append(swap(state, i, j, i + 1, j + 1, 'down-right'))
    if i > 0 and j > 0:
        neighbors.append(swap(state, i, j, i - 1, j - 1, 'up-left'))
    if i < len(state) - 1 and j > 0:
        neighbors.append(swap(state, i, j, i + 1, j - 1, 'down-left'))
    return neighbors

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '_':
                return i, j
    return None

def swap(state, i, j, ni, nj, action):
    new_state = [list(row) for row in state]
    new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
    return new_state, action

start = [['e', 'a', 'y', 'u', 'i', 'e'], ['m', 'k', 's', 'o', 'd', 'l'], ['c', 'a', '_', 'l', 'e', 'd'], ['g', 'l', 'r', 'o', 'u', 's']]
target = [['a', 'k', 'u', 'l', 'e', '_'], ['m', 'e', 's', 'o', 'd', 'e'], ['c', 'a', 'l', 'l', 'i', 'd'], ['g', 'y', 'r', 'o', 'u', 's']]
print(bfs(start, target))
