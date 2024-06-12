
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    seen = set()
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        for next_state, action in neighbors(state):
            if next_state not in seen:
                queue.append((next_state, path + [action]))
                seen.add(next_state)

def neighbors(state):
    i, j = next((i, j) for i in range(4) for j in range(4) if state[i][j] == '_')
    deltas = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    for di, dj in deltas:
        if 0 <= i + di < 4 and 0 <= j + dj < 4:
            next_state = [list(row) for row in state]
            next_state[i][j], next_state[i + di][j + dj] = next_state[i + di][j + dj], next_state[i][j]
            yield next_state, (i, j, i + di, j + dj)

start = [['_', 's', 'a', 'n'], ['q', 'u', 'o', 'u'], ['c', 'h', 'u', 't'], ['l', 't', 'r', 'e']]
target = [['s', 'u', 'n', '_'], ['q', 'u', 'o', 't'], ['c', 'h', 'a', 't'], ['l', 'u', 'r', 'e']]
print(bfs(start, target))
