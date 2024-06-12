
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, swaps = queue.popleft()
        if current == target:
            return swaps
        for i in range(len(current)):
            for j in range(len(current)):
                if current[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current) and 0 <= ny < len(current[0]):
                            new_board = [list(row) for row in current]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_state = ''.join([''.join(row) for row in new_board])
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, swaps + [((i, j), (nx, ny))]))
    return None

start = [['a', 'n', 'x', 'e'], ['c', 'y', 'l', 'a'], ['r', 'e', '_', 'n'], ['j', 'h', 'o', 'a'], ['e', 'x', 'b', 'm']]
target = ['nye', 'calx', 'hern', 'jaob', 'exam']

result = bfs(start, target)
print(result)
