
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
    directions = [(1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left'), (-1, 1, 'up-right')]
    blank = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    for dx, dy, direction in directions:
        x, y = blank[0] + dx, blank[1] + dy
        if 0 <= x < len(state) and 0 <= y < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[blank[0]][blank[1]], new_state[x][y] = new_state[x][y], new_state[blank[0]][blank[1]]
            yield (new_state, direction)

start = [['a', 'r', '_', 'c'], ['h', 'a', 'v', 'e'], ['a', 'g', 's', 'd'], ['b', 'i', 't', 'z']]
target = [['_', 'r', 'i', 'c'], ['h', 'a', 'v', 'e'], ['s', 'g', 'a', 'd'], ['b', 'a', 't', 'z']]
print(bfs(start, target))
