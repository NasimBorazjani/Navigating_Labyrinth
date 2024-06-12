
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for (next_state, direction) in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [direction]))
                seen.add(next_state)

def neighbors(state):
    directions = [(1, -1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (-1, 1, 'down-left')]
    blank = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_')
    for di, dj, direction in directions:
        ni, nj = blank[0] + di, blank[1] + dj
        if 0 <= ni < len(state) and 0 <= nj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[blank[0]][blank[1]], next_state[ni][nj] = next_state[ni][nj], next_state[blank[0]][blank[1]]
            yield (next_state, direction)

start = [['_', 'm', 'u', 'p'], ['c', 'e', 'r', 'a'], ['d', 'r', 'e', 'b'], ['v', 'e', 'l', 'o']]
goal = [['m', 'a', 'p', '_'], ['c', 'e', 'r', 'e'], ['d', 'r', 'u', 'b'], ['v', 'e', 'l', 'o']]

print(bfs(start, goal))
