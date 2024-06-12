
from collections import deque

def get_neighbors(state):
    directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    neighbors = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(state) and 0 <= nj < len(state[0]):
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append((new_state, (di, dj)))
    return neighbors

def bfs(initial, target):
    queue = deque([(initial, None, None)])
    visited = set()
    prev = {str(initial): (None, None)}
    while queue:
        state, _, _ = queue.popleft()
        if state == target:
            path = []
            while state is not None:
                state, action = prev[str(state)]
                path.append(action)
            return path[::-1][1:]
        for neighbor, action in get_neighbors(state):
            if str(neighbor) not in visited:
                queue.append((neighbor, state, action))
                visited.add(str(neighbor))
                prev[str(neighbor)] = (state, action)
    return None

initial = [['c', 'o', 'a', 'c'], ['i', 'o', 'h', 'r'], ['d', 'e', 'r', 'r'], ['f', 'o', 'u', 'a'], ['p', 'e', '_', 'i']]
target = [['_', 'o', 'r', 'c'], ['i', 'c', 'h', 'o'], ['d', 'e', 'a', 'r'], ['f', 'o', 'u', 'r'], ['p', 'e', 'a', 'i']]
actions = bfs(initial, target)
print(actions)
