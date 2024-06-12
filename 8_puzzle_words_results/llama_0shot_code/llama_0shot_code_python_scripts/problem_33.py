
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(board, None)])
    while queue:
        current_board, direction = queue.popleft()
        current_words = ''.join([''.join(row) for row in current_board])
        if current_words == ''.join(words):
            return direction
        for i in range(len(current_board)):
            for j in range(len(current_board[i])):
                if current_board[i][j] == '_':
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current_board) and 0 <= ny < len(current_board[i]) and current_board[nx][ny] != '_':
                            new_board = [row.copy() for row in current_board]
                            new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                            new_direction = (i, j, nx, ny)
                            if new_direction not in visited:
                                visited.add(new_direction)
                                queue.append((new_board, new_direction))
    return None

def get_directions(direction):
    if direction is None:
        return []
    x1, y1, x2, y2 = direction
    if x1 < x2 and y1 < y2:
        return ['down-right']
    elif x1 > x2 and y1 < y2:
        return ['up-right']
    elif x1 < x2 and y1 > y2:
        return ['down-left']
    else:
        return ['up-left']

initial_board = [['g', 'j', 'u', 'm', 'a'], ['a', 'r', 'o', 'e', 'o'], ['h', 'u', '_', 'g', 'd'], ['s', 'c', 'r', 'a', 'f']]
target_words = ['jama', 'agoho', 'rudge', 'scruf']

directions = bfs(initial_board, target_words)
print(get_directions(directions))
