
from collections import deque

def get_moves(state):
    empty = [(index, row.index('_')) for index, row in enumerate(state) if '_' in row][0]
    x, y = empty
    moves = []
    if x > 0: moves.append((x - 1, y))  # Move up
    if x < len(state) - 1: moves.append((x + 1, y))  # Move down
    if y > 0: moves.append((x, y - 1))  # Move left
    if y < len(state[0]) - 1: moves.append((x, y + 1))  # Move right
    return moves

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return [tuple(row) for row in state]

def bfs(initial_state):
    goal_state = sorted([item for sublist in initial_state for item in sublist if item != '_'], reverse=True)
    goal_state = [tuple(goal_state[i:i+6]) for i in range(0, len(goal_state), 6)] + [('_',)]
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for move in get_moves(state):
            new_state = swap(state, [(index, row.index('_')) for index, row in enumerate(state) if '_' in row][0], move)
            if new_state not in visited:
                queue.append((new_state, path + [state[move[0]][move[1]]]))
                visited.add(new_state)

initial_state = [(99, 98, 87, 84, 72, 64), (60, 59, 19, 57, '_'), (33, 22, 18, 48, 16, 37)]
print(bfs(initial_state))
