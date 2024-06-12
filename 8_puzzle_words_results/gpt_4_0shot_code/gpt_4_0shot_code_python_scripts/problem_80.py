
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set()
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
        for j, tile in enumerate(row):
            if tile == '_':
                return i, j

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in state)

start = (('d', 'w', 'p', 'l', 't'), ('e', 'i', 'd', 'e', 'c'), ('_', 'q', 'e', 'i', 'r'), ('m', 'e', 'c', 'u', 'r'), ('y', 'u', 'a', 't', 'a'))
target = (('w', 'e', 'l', 't', '_'), ('e', 'd', 'd', 'i', 'c'), ('e', 'q', 'u', 'i', 'p'), ('m', 'a', 'c', 'e', 'r'), ('y', 'u', 'r', 't', 'a'))
print(bfs(start, target))
