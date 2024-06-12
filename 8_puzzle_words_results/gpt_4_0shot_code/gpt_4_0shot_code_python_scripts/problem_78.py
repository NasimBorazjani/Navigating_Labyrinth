
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
    directions = [(i-1, j+1, 'up-right'), (i+1, j+1, 'down-right'), (i-1, j-1, 'up-left'), (i+1, j-1, 'down-left')]
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
    i1, j1 = pos1
    i2, j2 = pos2
    next_state = [list(row) for row in state]
    next_state[i1][j1], next_state[i2][j2] = next_state[i2][j2], next_state[i1][j1]
    return tuple(tuple(row) for row in next_state)

start = (('a', 'j', '_', 'k', 'e'), ('t', 's', 'w', 'y', 'e'), ('t', 'r', 'a', 'p', 'a'), ('s', 'e', 'a', 'm', 'h'), ('c', 'r', 's', 'e', 'p'))
goal = (('j', 'a', 'k', 'e', '_'), ('t', 'a', 'w', 's', 'e'), ('t', 'r', 'y', 'p', 'a'), ('s', 'm', 'a', 's', 'h'), ('c', 'r', 'e', 'e', 'p'))
print(bfs(start, goal))
