
from collections import deque

def bfs(init_board, target_words):
    moves = {'_': ['_', 'u', 'd', 'l', 'r']}
    for i in range(len(init_board)):
        for j in range(len(init_board[i])):
            if init_board[i][j] != '_':
                moves[init_board[i][j]] = [init_board[i][j]]
    target_state = '#'.join(target_words)
    init_state = '#'.join([''.join(row) for row in init_board])
    queue = deque([(init_state, [])])
    visited = set()
    while queue:
        state, swaps = queue.popleft()
        if state == target_state:
            return swaps
        for i in range(len(state)):
            if state[i] != '_':
                for j in range(i - 1, i + 2):
                    if 0 <= j < len(state) and state[j] in moves[state[i]]:
                        new_state = list(state)
                        new_state[i], new_state[j] = new_state[j], new_state[i]
                        new_state = ''.join(new_state)
                        new_swaps = swaps + [state[i] + state[j]]
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, new_swaps))
    return []

init_board = [['e', 'l', 'u', 'w'], ['k', 'k', 'c', 'e'], ['f', 'l', '_', 'a'], ['s', 'r', 's', 'e'], ['h', 'e', 'u', 'b']]
target_words = ['lew', 'keck', 'flea', 'susu', 'herb']
print(bfs(init_board, target_words))
