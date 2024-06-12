
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for (next_state, action) in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def neighbors(state):
    i, j = state.index('_'), state[0].index('_')
    deltas = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    for di, dj in deltas:
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield (next_state, (di, dj))

start = [['i', 'e', 'e', 'd'], ['v', 't', 'n', 'l'], ['o', 'd', '_', 'a'], ['p', 'r', 'c', 'e'], ['p', 'i', 'o', 'l']]
goal = [['_', 'e', 'l', 'd'], ['v', 'i', 'n', 't'], ['e', 'd', 'e', 'a'], ['p', 'o', 'c', 'o'], ['p', 'i', 'r', 'l']]
print(bfs(start, goal))
