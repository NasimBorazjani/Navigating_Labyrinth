
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for (next_state, direction) in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [direction]))
                seen.add(next_state)

def neighbors(state):
    i, j = find_blank(state)
    directions = [(i-1, j-1, 'up-left'), (i-1, j+1, 'up-right'), (i+1, j-1, 'down-left'), (i+1, j+1, 'down-right')]
    for i2, j2, direction in directions:
        if i2 >= 0 and i2 < len(state) and j2 >= 0 and j2 < len(state[0]):
            next_state = swap(state, (i, j), (i2, j2))
            yield (next_state, direction)

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '_':
                return i, j

def swap(state, pos1, pos2):
    i1, j1 = pos1
    i2, j2 = pos2
    next_state = [list(row) for row in state]
    next_state[i1][j1], next_state[i2][j2] = next_state[i2][j2], next_state[i1][j1]
    return next_state

start = [['l', 'a', 'e', 'o', 'n'], ['p', 'z', 'i', 'n', 'r'], ['l', 'a', 'g', 'o', '_'], ['i', 'e', 'e', 'u', 'm']]
target = [['_', 'a', 'e', 'o', 'n'], ['p', 'l', 'i', 'e', 'r'], ['g', 'a', 'z', 'o', 'n'], ['i', 'l', 'e', 'u', 'm']]
print(bfs(start, target))
