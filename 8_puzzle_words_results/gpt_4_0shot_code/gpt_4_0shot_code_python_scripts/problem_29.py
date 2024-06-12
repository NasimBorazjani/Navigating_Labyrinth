
from collections import deque

def bfs(initial, target):
    queue = deque([(initial, [])])
    visited = {tuple(map(tuple, initial)): None}
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank = [(i, j) for i in range(4) for j in range(5) if state[i][j] == '_'][0]
        for di, dj, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            ni, nj = blank[0] + di, blank[1] + dj
            if 0 <= ni < 4 and 0 <= nj < 5:
                new_state = [list(row) for row in state]
                new_state[blank[0]][blank[1]], new_state[ni][nj] = new_state[ni][nj], new_state[blank[0]][blank[1]]
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    queue.append((new_state, path + [direction]))
                    visited[new_state_tuple] = (state, direction)

initial = [['d', 't', 's', 'l', 'a'], ['u', 'a', 'a', 'e', 'i'], ['_', 'l', 'g', 'i', 'a'], ['w', 'r', 'n', 'c', 'h']]
target = [['t', 'a', 'l', 'a', '_'], ['u', 'd', 'a', 's', 'i'], ['g', 'l', 'a', 'i', 'r'], ['w', 'e', 'n', 'c', 'h']]
print(bfs(initial, target))
