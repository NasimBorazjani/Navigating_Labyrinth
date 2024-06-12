
from collections import deque

def bfs(initial, target):
    queue = deque([initial])
    visited = set([initial])
    parent = {initial: (None, None)}
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current is not None:
                path.append(parent[current][1])
                current = parent[current][0]
            return list(reversed(path[1:]))
        for next_state, action in get_neighbors(current):
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                parent[next_state] = (current, action)

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
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, i1, j1, i2, j2, action):
    new_state = [list(row) for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return tuple(map(tuple, new_state)), action

initial = (('a', 'a', 'e', 'e', 'y'), ('h', 'a', 'i', 't', 'h'), ('_', 'r', 'k', 'n', 't'), ('m', 'k', 'n', 'o', 'o'))
target = (('a', 'k', 'e', 'y', '_'), ('h', 'a', 'i', 'k', 'h'), ('t', 'r', 'o', 'n', 'e'), ('m', 'a', 'n', 't', 'o'))
print(bfs(initial, target))
