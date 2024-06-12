
import heapq
import numpy as np

def heuristic(a, b):
    return np.sum(np.abs(a - b))

def solve_puzzle(start, goal):
    stack = [(0, start)]
    seen = set()
    while stack:
        (cost, current) = heapq.heappop(stack)
        if np.array_equal(current, goal):
            return cost
        for action in ['up', 'down', 'left', 'right']:
            next_state = move(current, action)
            if next_state is not None and str(next_state) not in seen:
                priority = cost + heuristic(next_state, goal)
                heapq.heappush(stack, (priority, next_state))
                seen.add(str(next_state))
    return None

def move(state, action):
    state = state.copy()
    i, j = np.where(state == '_')
    if action == 'up' and i > 0:
        state[i, j], state[i-1, j] = state[i-1, j], state[i, j]
    elif action == 'down' and i < 2:
        state[i, j], state[i+1, j] = state[i+1, j], state[i, j]
    elif action == 'left' and j > 0:
        state[i, j], state[i, j-1] = state[i, j-1], state[i, j]
    elif action == 'right' and j < 2:
        state[i, j], state[i, j+1] = state[i, j+1], state[i, j]
    else:
        return None
    return state

start = np.array([[30, 12, 67], [21, '_', 28], [80, 16, 37]])
goal = np.array([[80, 67, 37], [30, 28, 16], [21, 12, '_']])
print(solve_puzzle(start, goal))
