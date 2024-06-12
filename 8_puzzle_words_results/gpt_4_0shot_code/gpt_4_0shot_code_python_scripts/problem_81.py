
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
    i, j = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_')
    for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield next_state, action

start = [['e', 'c', 'o', 'r', 'e'], ['r', 'e', 'u', 't', 'l'], ['r', 'i', 'i', 'c', 'i'], ['k', 'n', 'z', 'e', 'l'], ['i', 'z', 'h', 'l', '_']]
goal = [['_', 'c', 'o', 'r', 'e'], ['r', 'e', 'u', 'e', 'l'], ['r', 'i', 'n', 'c', 'h'], ['k', 'i', 'z', 'i', 'l'], ['i', 'z', 't', 'l', 'e']]
print(bfs(start, goal))
