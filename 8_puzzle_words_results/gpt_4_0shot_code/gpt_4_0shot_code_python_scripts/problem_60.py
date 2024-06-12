
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([str(start)])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, direction in get_neighbors(state):
            if str(next_state) not in seen:
                queue.append((next_state, path + [direction]))
                seen.add(str(next_state))
    return []

def get_neighbors(state):
    neighbors = []
    i, j = find_blank(state)
    if i > 0 and j < len(state[0]) - 1:
        swap(state, i, j, i - 1, j + 1)
        neighbors.append((state[:], 'up-right'))
        swap(state, i, j, i - 1, j + 1)
    if i < len(state) - 1 and j < len(state[0]) - 1:
        swap(state, i, j, i + 1, j + 1)
        neighbors.append((state[:], 'down-right'))
        swap(state, i, j, i + 1, j + 1)
    if i > 0 and j > 0:
        swap(state, i, j, i - 1, j - 1)
        neighbors.append((state[:], 'up-left'))
        swap(state, i, j, i - 1, j - 1)
    if i < len(state) - 1 and j > 0:
        swap(state, i, j, i + 1, j - 1)
        neighbors.append((state[:], 'down-left'))
        swap(state, i, j, i + 1, j - 1)
    return neighbors

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j
    return -1, -1

def swap(state, i1, j1, i2, j2):
    state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]

start = [['e', 'b', 'a', 'n'], ['z', 'e', 'e', 'd'], ['o', 'a', 'd', 'y'], ['m', 'u', 't', 'z'], ['m', 'a', '_', 'n']]
target = [['_', 'b', 'a', 'n'], ['z', 'e', 'e', 'd'], ['d', 'a', 'z', 'y'], ['m', 'o', 't', 'e'], ['m', 'a', 'u', 'n']]
print(bfs(start, target))
