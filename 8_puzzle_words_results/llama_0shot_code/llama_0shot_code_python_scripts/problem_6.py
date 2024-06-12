
from collections import deque

def bfs(initial_board, target_words):
    initial_state = ''.join([''.join(row) for row in initial_board])
    target_state = ''.join(target_words)
    queue = deque([(initial_state, '')])
    visited = set()
    directions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}

    while queue:
        current_state, swaps = queue.popleft()
        if current_state == target_state:
            return swaps
        for direction, (dr, dc) in directions.items():
            for r in range(1, len(initial_board)):
                for c in range(1, len(initial_board[0])):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(initial_board) and 0 <= nc < len(initial_board[0]) and current_state[nr * len(initial_board[0]) + nc] == '_':
                        new_state = list(current_state)
                        new_state[r * len(initial_board[0]) + c], new_state[nr * len(initial_board[0]) + nc] = new_state[nr * len(initial_board[0]) + nc], new_state[r * len(initial_board[0]) + c]
                        new_state = ''.join(new_state)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, swaps + ' ' + direction))

    return None

initial_board = [['l', 'c', '_', 'o'], ['s', 'c', 'o', 'h'], ['d', 'y', 'a', 'e'], ['h', 's', 'l', 't']]
target_words = ['cho', 'slod', 'syce', 'halt']
print(bfs(initial_board, target_words))
