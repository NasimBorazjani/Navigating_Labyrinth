
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        current, swaps = queue.popleft()
        if current == target:
            return swaps
        if current not in visited:
            visited.add(current)
            for i in range(len(current)):
                for j in range(len(current[i])):
                    if current[i][j] == '_':
                        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                            x, y = i + dx, j + dy
                            if 0 <= x < len(current) and 0 <= y < len(current[0]):
                                new_board = [row.copy() for row in current]
                                new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
                                queue.append((new_board, swaps + [(i, j, x, y)]))

    return None

start = [['a', 'm', '_', 'p'], ['p', 'e', 'h', 'a'], ['l', 'e', 'y', 'l'], ['v', 'i', 'a', 'i'], ['w', 'u', 's', 'p']]
target = ['map', 'pahi', 'yeel', 'vial', 'wusp']

result = bfs(start, [list(word) for word in target])
print(result)
