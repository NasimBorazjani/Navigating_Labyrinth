
from collections import deque

def find_path(start, target):
    queue = deque([(start, [])])
    visited = {tuple(map(tuple, start)): None}
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank = [(i, j) for i in range(5) for j in range(6) if state[i][j] == '_'][0]
        for di, dj, dir in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = blank[0] + di, blank[1] + dj
            if 0 <= ni < 5 and 0 <= nj < 6:
                new_state = [list(row) for row in state]
                new_state[blank[0]][blank[1]], new_state[ni][nj] = new_state[ni][nj], new_state[blank[0]][blank[1]]
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    queue.append((new_state, path + [dir]))
                    visited[new_state_tuple] = (state, dir)
    return []

start = [['e', 's', '_', 'r', 'k', 'w'], ['b', 'c', 'd', 'd', 'r', 'a'], ['c', 'u', 'e', 'c', 'e', 's'], ['b', 'r', 'n', 'h', 'e', 'a'], ['h', 'o', 'e', 'k', 'r', 'r']]
target = [['_', 's', 'h', 'r', 'e', 'w'], ['b', 'e', 'd', 'a', 'r', 'k'], ['c', 'u', 'r', 'c', 'a', 's'], ['b', 'e', 'n', 'd', 'e', 'r'], ['h', 'o', 'c', 'k', 'e', 'r']]
print(find_path(start, target))
