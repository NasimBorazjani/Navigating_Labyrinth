
from collections import deque

def bfs(start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: (None, None)}
    while queue:
        state = queue.popleft()
        if state == target:
            path = []
            while state is not None:
                path.append(parent[state][1])
                state = parent[state][0]
            return path[::-1][1:]
        for next_state, action in neighbors(state):
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                parent[next_state] = (state, action)
    return None

def neighbors(state):
    i, j = find_blank(state)
    for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield tuple(map(tuple, next_state)), action

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '_':
                return i, j

start = (('t', 'd', 'u', 'k', 'e'), ('a', 'a', 'o', 'l', 'l'), ('a', 'm', '_', 'z', 'i'), ('n', 'e', 'u', 'y', 'n'))
target = (('d', 'y', 'k', 'e', '_'), ('a', 't', 'o', 'l', 'l'), ('a', 'm', 'u', 'z', 'e'), ('n', 'i', 'u', 'a', 'n'))
print(bfs(start, target))
