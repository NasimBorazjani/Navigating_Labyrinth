
from collections import deque

def bfs(initial, target):
    queue = deque([initial])
    visited = set([tuple(map(tuple, initial))])
    parent = {tuple(map(tuple, initial)): (None, None)}
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current:
                current, action = parent[tuple(map(tuple, current))]
                if action:
                    path.append(action)
            return path[::-1]
        i, j = next((i, j) for i, row in enumerate(current) for j, cell in enumerate(row) if cell == '_')
        for di, dj, action in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(current) and 0 <= nj < len(current[0]):
                next_state = [list(row) for row in current]
                next_state[i][j], next_state[ni][nj] = next_state[ni][nj], next_state[i][j]
                if tuple(map(tuple, next_state)) not in visited:
                    queue.append(next_state)
                    visited.add(tuple(map(tuple, next_state)))
                    parent[tuple(map(tuple, next_state))] = (current, action)
    return []

initial = [['_', 's', 's', 'h', 'o'], ['r', 'i', 'l', 'o', 'y'], ['j', 'o', 'l', 'i', 'p'], ['d', 'r', 'a', 'i', 'n'], ['n', 'i', 'v', 'a', 'l']]
target = [['s', 'o', 'h', 'o', '_'], ['r', 'i', 'l', 'l', 'y'], ['j', 'o', 's', 'i', 'p'], ['d', 'r', 'a', 'i', 'n'], ['n', 'i', 'v', 'a', 'l']]
print(bfs(initial, target))
