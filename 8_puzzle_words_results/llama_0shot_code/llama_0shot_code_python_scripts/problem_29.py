
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
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < len(current) and 0 <= ny < len(current[0]):
                                new_board = [list(row) for row in current]
                                new_board[i][j], new_board[nx][ny] = new_board[nx][ny], new_board[i][j]
                                new_board[i] = ''.join(new_board[i])
                                new_board[nx] = ''.join(new_board[nx])
                                new_state = '\n'.join(new_board)
                                queue.append((new_state, swaps + [f"{i+1},{j+1}->{nx+1},{ny+1}"]))
        else:
            continue
    return None

start = ['dt_sl_a', 'u_aa_ei', 'l_g_ia', 'wr_nch']
target = ['t_ala', 'ud_asi', 'g_lair', 'wen_ch']

result = bfs('\n'.join(start), '\n'.join(target))
print(result)
