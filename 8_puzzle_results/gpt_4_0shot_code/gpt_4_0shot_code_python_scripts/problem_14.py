
from collections import deque

def get_moves(state):
    moves = []
    i, j = state.index('_'), state[state.index('_')].index('_')
    if i > 0: moves.append((i-1, j))
    if i < 2: moves.append((i+1, j))
    if j > 0: moves.append((i, j-1))
    if j < 2: moves.append((i, j+1))
    return moves

def bfs(start):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for move in get_moves(state):
            next_state = swap(state, move)
            if str(next_state) not in seen:
                queue.append((next_state, path + [state[move[0]][move[1]]]))
                seen.add(str(next_state))

def swap(state, move):
    i, j = state.index('_'), state[state.index('_')].index('_')
    next_state = [row[:] for row in state]
    next_state[i][j], next_state[move[0]][move[1]] = next_state[move[0]][move[1]], next_state[i][j]
    return next_state

start = [[28, 51, 19], [89, '_', 21], [43, 39, 45]]
goal = [[89, 51, 45], [43, 39, 28], [21, 19, '_']]
print(bfs(start))
