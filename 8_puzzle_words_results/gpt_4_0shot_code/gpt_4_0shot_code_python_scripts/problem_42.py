
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
    return []

def get_neighbors(state):
    neighbors = []
    i, j = find_blank(state)
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

def swap(state, i, j, new_i, new_j, direction):
    new_state = [list(row) for row in state]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state, direction

start = [['_', 'j', 'a', 'r', 'e', 'b'], ['z', 'o', 'y', 's', 'i', 'i'], ['r', 'e', 'r', 's', 't', 'y'], ['g', 'e', 'i', 'q', 'u', 'a']]
target = [['j', 'e', 'r', 'i', 'b', '_'], ['z', 'o', 'y', 's', 'i', 'a'], ['r', 'e', 'e', 's', 't', 'y'], ['g', 'r', 'i', 'q', 'u', 'a']]
print(bfs(start, target))
