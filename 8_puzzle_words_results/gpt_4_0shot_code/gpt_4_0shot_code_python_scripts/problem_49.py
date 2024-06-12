
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
    i, j = find_blank(state)
    neighbors = []
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

def swap(state, i, j, x, y):
    state[i][j], state[x][y] = state[x][y], state[i][j]

start = [['a', 'l', 'o', 'a', 'm', 'h'], ['f', 'e', 'n', 'n', 'a', 't'], ['t', 'r', 'a', 'g', '_', 'c'], ['c', 'i', 'r', 'a', 'n', 'e']]
target = [['_', 'l', 'e', 'a', 't', 'h'], ['f', 'a', 'n', 'm', 'a', 'n'], ['t', 'r', 'a', 'g', 'i', 'c'], ['c', 'a', 'r', 'o', 'n', 'e']]
print(bfs(start, target))
