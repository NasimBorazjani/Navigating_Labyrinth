
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, action in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def neighbors(state):
    i, j = find_blank(state)
    swaps = [(i-1, j-1, 'up-left'), (i-1, j+1, 'up-right'), (i+1, j-1, 'down-left'), (i+1, j+1, 'down-right')]
    for i2, j2, action in swaps:
        if 0 <= i2 < len(state) and 0 <= j2 < len(state[0]):
            next_state = swap(state, (i, j), (i2, j2))
            yield next_state, action

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '_':
                return i, j

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in state)

start = (('p', 'j', 'm', 'y'), ('e', 'h', 'p', 'o'), ('y', 'o', '_', 'e'), ('r', 'a', 'o', 'n'), ('w', 'a', 'r', 'd'))
goal = (('j', 'a', 'y', '_'), ('e', 'p', 'p', 'y'), ('h', 'o', 'm', 'e'), ('r', 'o', 'o', 'n'), ('w', 'a', 'r', 'd'))
print(bfs(start, goal))
