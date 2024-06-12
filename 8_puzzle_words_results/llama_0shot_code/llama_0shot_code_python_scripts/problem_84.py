
from collections import deque

def bfs(init_board, target_words):
    moves = [('u', 0, -1), ('d', 0, 1), ('l', -1, 0), ('r', 1, 0)]
    target_state = '#'.join(target_words)
    visited = set()
    queue = deque([(str(init_board), '')])
    while queue:
        current_state, swaps = queue.popleft()
        if current_state == target_state:
            return swaps
        current_board = [list(word) for word in current_state.split('#')]
        for i in range(len(moves)):
            direction, dr, dc = moves[i]
            for r in range(1, len(current_board)):
                for c in range(len(current_board[0])):
                    if current_board[r][c] == '_':
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(current_board) and 0 <= nc < len(current_board[0]) and current_board[nr][nc] != '_':
                            new_board = [list(row) for row in current_board]
                            new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                            new_state = '#'.join([''.join(row) for row in new_board])
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, swaps + direction))
    return None

init_board = [['e', 'r', 'p', 't', 'o'], ['s', 't', 'r', 'k', 'r'], ['e', 'a', '_', 'a', 'i'], ['d', 'o', 'n', 's', 'a'], ['d', 'e', 's', 'e', 'x']]
target_words = ['roto', 'serer', 'tapas', 'dinka', 'desex']
print(bfs(init_board, target_words))
