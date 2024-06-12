
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for (t, action) in neighbors(state):
            if t not in seen:
                queue.append((t, path + [action]))
                seen.add(t)

def neighbors(state):
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    swaps = [(i-1, j+1, 'up-right'), (i+1, j+1, 'down-right'), (i-1, j-1, 'up-left'), (i+1, j-1, 'down-left')]
    return [(swap(state, (i, j), (i+di, j+dj)), action) for di, dj, action in swaps if 0 <= i+di < len(state) and 0 <= j+dj < len(state[0])]

def swap(state, p1, p2):
    state = [list(row) for row in state]
    state[p1[0]][p1[1]], state[p2[0]][p2[1]] = state[p2[0]][p2[1]], state[p1[0]][p1[1]]
    return tuple(map(tuple, state))

start = (('a', 's', '_', 'p', 'e'), ('c', 'u', 'd', 'o', 's'), ('l', 'u', 'u', 'a', 's'), ('r', 'c', 'u', 'n', 'e'))
goal = (('s', 'u', 'p', 'e', '_'), ('c', 'a', 'd', 'u', 's'), ('n', 'u', 'c', 'a', 'l'), ('r', 'o', 'u', 's', 'e'))

print(bfs(start, goal))
