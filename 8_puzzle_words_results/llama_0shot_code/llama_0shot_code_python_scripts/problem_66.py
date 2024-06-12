
from collections import deque

def bfs(board, words):
    start = tuple(map(tuple, board))
    target = tuple(map(tuple, [list(word) for word in words]))
    queue = deque([(start, 0, 0)])  # (state, distance, moves)
    visited = {start}
    directions = {'up-right': (-1, 1), 'down-right': (1, 1), 'up-left': (-1, -1), 'down-left': (1, -1)}

    while queue:
        state, distance, moves = queue.popleft()
        if state == target:
            return moves

        blank = state.index(('_',))
        for direction, (dr, dc) in directions.items():
            nr, nc = blank // len(board[0]), blank % len(board[0])
            nr += dr
            nc += dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                new_state = list(map(list, state))
                new_state[nr][nc], new_state[blank // len(board[0])][blank % len(board[0])] = new_state[blank // len(board[0])][blank % len(board[0])], new_state[nr][nc]
                new_state = tuple(map(tuple, new_state))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, distance + abs(nr - blank // len(board[0])) + abs(nc - blank % len(board[0])), moves + 1))

    return -1

board = [['p', 'j', 'm', 'y'], ['e', 'h', 'p', 'o'], ['y', 'o', '_', 'e'], ['r', 'a', 'o', 'n'], ['w', 'a', 'r', 'd']]
words = ['jay', 'eppy', 'home', 'roon', 'ward']
print(bfs(board, words))
