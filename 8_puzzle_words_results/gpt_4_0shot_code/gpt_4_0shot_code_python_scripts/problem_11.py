
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
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in state)

start = (('o', 'b', 'e', 'd'), ('c', 'o', 'd', 'u'), ('w', 'a', '_', 'p'), ('y', 'u', 'l', 'p'))
goal = (('b', 'u', 'd', '_'), ('c', 'o', 'd', 'o'), ('w', 'a', 'u', 'p'), ('y', 'e', 'l', 'p'))
print(bfs(start, goal))
