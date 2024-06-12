
from collections import deque

def get_neighbors(state):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    neighbors = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(state) and 0 <= nj < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def bfs(start, goal):
    queue = deque([(start, [])])
    seen = {str(start)}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for neighbor in get_neighbors(state):
            if str(neighbor) not in seen:
                queue.append((neighbor, path + [neighbor]))
                seen.add(str(neighbor))

start = [['y', 'c', 'a', 'r', 'd'], ['s', 'u', 'l', 'c', 'a'], ['v', 'h', '_', 'n', 'o'], ['s', 'e', 'l', 's', 'm'], ['b', 'i', 'u', 'h', 'y']]
goal = [['_', 'c', 'a', 'r', 'd'], ['s', 'y', 'l', 'v', 'a'], ['s', 'h', 'u', 'n', 'e'], ['s', 'o', 'l', 'u', 'm'], ['b', 'i', 'c', 'h', 'y']]
print(bfs(start, goal))
