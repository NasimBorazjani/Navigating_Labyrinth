
from collections import deque

def get_neighbors(state):
    i, j = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]
    neighbors = []
    if i > 0 and j < len(state[0]) - 1:
        neighbors.append((i - 1, j + 1))  # up-right
    if i < len(state) - 1 and j < len(state[0]) - 1:
        neighbors.append((i + 1, j + 1))  # down-right
    if i > 0 and j > 0:
        neighbors.append((i - 1, j - 1))  # up-left
    if i < len(state) - 1 and j > 0:
        neighbors.append((i + 1, j - 1))  # down-left
    return neighbors

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set([str(start)])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for i, j in get_neighbors(state):
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[i - 1][j + 1] = new_state[i - 1][j + 1], new_state[i][j]
            if str(new_state) not in seen:
                queue.append((new_state, path + [(i, j)]))
                seen.add(str(new_state))

start = [['e', 'b', 'v', 'r', 'l', 't'], ['m', 'u', 'r', 'm', 'i', 'r'], ['h', 'o', 'a', 'a', '_', 'e'], ['c', 'n', 'i', 's', 'e', 's'], ['t', 'i', 'l', 'p', 'y', 'h']]
target = [['_', 'b', 'u', 'r', 's', 't'], ['m', 'e', 'r', 'r', 'i', 'l'], ['m', 'o', 'n', 'a', 's', 'e'], ['c', 'h', 'i', 'v', 'e', 'y'], ['t', 'i', 'l', 'p', 'a', 'h']]
print(bfs(start, target))
