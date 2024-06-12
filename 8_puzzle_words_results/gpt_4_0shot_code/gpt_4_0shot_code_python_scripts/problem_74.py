
from collections import deque

def bfs(board, target):
    queue = deque([(board, [])])
    visited = set([str(board)])
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        blank = [(i, j) for i in range(5) for j in range(5) if state[i][j] == '_'][0]
        for dx, dy, direction in [(-1, 1, 'up-right'), (1, 1, 'down-right'), (-1, -1, 'up-left'), (1, -1, 'down-left')]:
            nx, ny = blank[0] + dx, blank[1] + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                new_state = [row[:] for row in state]
                new_state[blank[0]][blank[1]], new_state[nx][ny] = new_state[nx][ny], new_state[blank[0]][blank[1]]
                if str(new_state) not in visited:
                    queue.append((new_state, path + [direction]))
                    visited.add(str(new_state))

target = [['z', 'e', 't', 'a', '_'], ['s', 'u', 'm', 'a', 'c'], ['s', 'h', 'o', 'w', 'y'], ['s', 'm', 'e', 'e', 'k'], ['a', 'j', 'a', 'v', 'a']]
board = [['u', 'z', 's', 't', 'a'], ['s', 'e', 'm', 'o', 'c'], ['a', 'h', '_', 'w', 'y'], ['s', 'a', 'e', 'm', 'k'], ['a', 'j', 'e', 'v', 'a']]
print(bfs(board, target))
