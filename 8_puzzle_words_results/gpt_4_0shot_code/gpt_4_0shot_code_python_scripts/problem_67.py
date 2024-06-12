
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = {tuple(map(tuple, start)): None}
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank = [(i, j) for i in range(4) for j in range(4) if state[i][j] == '_'][0]
        for di, dj, dir in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = blank[0] + di, blank[1] + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                new_state = [list(row) for row in state]
                new_state[blank[0]][blank[1]], new_state[ni][nj] = new_state[ni][nj], new_state[blank[0]][blank[1]]
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    queue.append((new_state, path + [dir]))
                    visited[new_state_tuple] = (state, dir)
    return []

start = [['e', 'l', 'u', 'w'], ['k', 'k', 'c', 'e'], ['f', 'l', '_', 'a'], ['s', 'r', 's', 'e'], ['h', 'e', 'u', 'b']]
target = [['_', 'l', 'e', 'w'], ['k', 'e', 'c', 'k'], ['f', 'l', 'e', 'a'], ['s', 'u', 's', 'u'], ['h', 'e', 'r', 'b']]
print(bfs(start, target))
