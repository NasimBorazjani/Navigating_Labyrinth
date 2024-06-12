
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([tuple(map(tuple, start))])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for (next_state, direction) in neighbors(state):
            if tuple(map(tuple, next_state)) not in seen:
                queue.append((next_state, path + [direction]))
                seen.add(tuple(map(tuple, next_state)))

def neighbors(state):
    directions = [(1, -1), (-1, 1), (1, 1), (-1, -1)]
    names = ['down-left', 'up-right', 'down-right', 'up-left']
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    for ((di, dj), direction) in zip(directions, names):
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield (next_state, direction)

start = [['u', 't', '_', 'e'], ['j', 'd', 'd', 'u'], ['o', 'e', 'z', 'n'], ['b', 'i', 'r', 'y'], ['w', 'i', 'r', 'y']]
goal = [['_', 't', 'u', 'e'], ['j', 'u', 'd', 'y'], ['z', 'e', 'i', 'n'], ['b', 'o', 'r', 'd'], ['w', 'i', 'r', 'y']]
print(bfs(start, goal))
