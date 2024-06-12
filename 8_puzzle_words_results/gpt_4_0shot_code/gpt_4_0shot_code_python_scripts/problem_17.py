
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, action in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def neighbors(state):
    i, j = find_blank(state)
    for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = swap(state, (i, j), (i + di, j + dj))
            yield next_state, action

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
    return tuple(map(tuple, next_state))

start = (('e', 'h', 'r', 'y'), ('w', 'f', 'r', 'r'), ('_', 'u', 'd', 'd'), ('f', 'a', 'i', 'b'))
target = (('h', 'a', 'y', '_'), ('w', 'e', 'r', 'f'), ('r', 'u', 'd', 'd'), ('f', 'r', 'i', 'b'))
print(bfs(start, target))
