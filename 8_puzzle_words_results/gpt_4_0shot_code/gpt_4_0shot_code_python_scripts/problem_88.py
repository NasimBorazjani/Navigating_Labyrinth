
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
    deltas = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    actions = ['up-right', 'down-right', 'up-left', 'down-left']

    for delta, action in zip(deltas, actions):
        di, dj = delta
        if 0 <= i + di < len(state) and 0 <= j + dj < len(state[0]):
            next_state = swap(state, (i, j), (i + di, j + dj))
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

start = (('g', 'f', 't', 'i', 'm'), ('a', 'l', 'a', 'a', 'e'), ('n', 's', '_', 'i', 'e'), ('f', 'p', 'o', 'k', 'y'), ('z', 'o', 'r', 'a', 'r'))
goal = (('f', 'r', 'i', 'm', '_'), ('a', 'g', 'a', 't', 'e'), ('a', 's', 'k', 'i', 'p'), ('f', 'l', 'o', 'e', 'y'), ('z', 'o', 'n', 'a', 'r'))

print(bfs(start, goal))
