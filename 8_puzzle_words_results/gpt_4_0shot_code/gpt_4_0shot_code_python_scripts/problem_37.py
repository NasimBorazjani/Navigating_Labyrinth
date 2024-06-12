
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
    actions = ['up-right', 'down-right', 'up-left', 'down-left']
    for delta, action in zip(deltas, actions):
        di, dj = delta
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield (next_state, action)

start = [['e', 'u', 'n', 'a', '_', 'e'], ['d', 'r', 'a', 'v', 'i', 'e'], ['m', 'a', 'n', 'u', 'k', 'a'], ['k', 'h', 'a', 't', 'u', 'm']]
goal = [['_', 'u', 'v', 'a', 't', 'e'], ['d', 'e', 'a', 'r', 'i', 'e'], ['m', 'a', 'n', 'u', 'k', 'a'], ['k', 'h', 'a', 'n', 'u', 'm']]
print(bfs(start, goal))
