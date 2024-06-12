
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
    i, j = state.index('_'), state[0].index('_')
    directions = [(i-1, j+1, 'up-right'), (i+1, j+1, 'down-right'), (i-1, j-1, 'up-left'), (i+1, j-1, 'down-left')]
    result = []
    for dx, dy, direction in directions:
        if 0 <= dx < len(state) and 0 <= dy < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[dx][dy] = next_state[dx][dy], next_state[i][j]
            result.append((next_state, direction))
    return result

start = [['o', 'f', '_', 'c', 'k'], ['s', 'n', 'f', 's', 'a'], ['o', 'i', 'i', 's', 'e'], ['n', 'e', 's', 'a', 'y']]
goal = [['f', 'a', 'c', 'k', '_'], ['s', 'o', 'f', 'i', 'a'], ['n', 'i', 's', 's', 'e'], ['n', 'o', 's', 'e', 'y']]
print(bfs(start, goal))
