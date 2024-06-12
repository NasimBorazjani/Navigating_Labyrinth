
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
    directions = [(1, -1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'down-left')]
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    return [((swap(state, (i, j), (i + di, j + dj)), direction) for di, dj, direction in directions if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]))]

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(map(tuple, state))

start = (('o', 's', 'n', 'e', 'd', 'a'), ('l', 'k', 'c', 'c', 'e', 'h'), ('t', 'o', '_', 'c', 'n', 'e'), ('c', 'i', 'l', 'a', 'i', 'c'), ('b', 'l', 'e', 'n', 'c', 'o'))
target = (('s', 'i', 'e', 'n', 'a', '_'), ('l', 'o', 'c', 'k', 'e', 'd'), ('c', 'o', 'n', 'c', 'h', 'e'), ('c', 'e', 'l', 't', 'i', 'c'), ('b', 'l', 'a', 'n', 'c', 'o'))

print(bfs(start, target))
