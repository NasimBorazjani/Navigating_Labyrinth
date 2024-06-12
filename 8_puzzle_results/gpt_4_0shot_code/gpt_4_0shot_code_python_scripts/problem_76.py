
from heapq import heappop, heappush

def get_moves(state):
    moves = []
    i, j = state.index('_')
    if i > 0: moves.append((i-1, j))
    if i < 2: moves.append((i+1, j))
    if j > 0: moves.append((i, j-1))
    if j < 4: moves.append((i, j+1))
    return moves

def swap(state, pos):
    i, j = state.index('_')
    state[i][j], state[pos[0]][pos[1]] = state[pos[0]][pos[1]], state[i][j]
    return state

def solve(initial):
    goal = [[86, 78, 77, 76, 39], [54, 45, 43, 46, 27], [38, 25, 21, 59, '_']]
    queue = [(0, initial, [])]
    seen = set()
    while queue:
        cost, state, path = heappop(queue)
        if state == goal:
            return path
        for move in get_moves(state):
            next_state = swap(state[:], move)
            if str(next_state) not in seen:
                seen.add(str(next_state))
                next_path = path + [next_state[move[0]][move[1]]]
                next_cost = cost + 1 + sum(abs(b - a) for a, b in zip(sum(next_state, []), sum(goal, [])))
                heappush(queue, (next_cost, next_state, next_path))
    return []

initial = [[86, 78, 77, 39, 76], [54, 45, 25, 59, 21], [38, 46, 43, 27, '_']]
print(solve(initial))
