
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
    i, j = find_blank(state)
    directions = [(i-1, j-1, 'up-left'), (i-1, j+1, 'up-right'), (i+1, j-1, 'down-left'), (i+1, j+1, 'down-right')]
    result = []
    for x, y, direction in directions:
        if 0 <= x < len(state) and 0 <= y < len(state[0]):
            next_state = swap(state, (i, j), (x, y))
            result.append((next_state, direction))
    return result

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(map(tuple, state))

start = (('r', 'u', 'p', 'f', 'y', 'w'), ('b', 'l', 'o', 'e', 'l', 'o'), ('n', 'r', '_', 'g', 'h', 't'), ('u', 'b', 'r', 'i', 'o', 't'))
goal = (('u', 'n', 'f', 'e', 'w', '_'), ('b', 'r', 'o', 'l', 'l', 'y'), ('b', 'r', 'i', 'g', 'h', 't'), ('u', 'p', 'r', 'o', 'o', 't'))
print(bfs(start, goal))
