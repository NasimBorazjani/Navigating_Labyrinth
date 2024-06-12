
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, direction in get_neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [direction]))
                seen.add(next_state)

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
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, i, j, new_i, new_j, direction):
    new_state = [list(row) for row in state]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state, direction

start = [['t', 'w', 'y', 'l', '_'], ['s', 'a', 'u', 'f', 't'], ['o', 'a', 'e', 'm', 'n'], ['f', 'l', 'd', 'm', 'd']]
target = [['_', 'w', 'o', 'l', 'f'], ['s', 't', 'u', 'n', 't'], ['l', 'a', 'm', 'm', 'y'], ['f', 'a', 'd', 'e', 'd']]
print(bfs(start, target))
