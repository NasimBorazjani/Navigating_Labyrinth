
import heapq
import numpy as np

def heuristic(a, b):
    return np.sum(np.abs(a - b))

def solve_puzzle(start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    visited = set()
    while queue:
        cost, current = heapq.heappop(queue)
        if np.array_equal(current, goal):
            return cost
        if str(current) in visited:
            continue
        visited.add(str(current))
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = np.where(current == '_')
            x, y = x[0], y[0]
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if 0 <= nx < current.shape[0] and 0 <= ny < current.shape[1]:
                next_state = current.copy()
                next_state[x][y], next_state[nx][ny] = next_state[nx][ny], next_state[x][y]
                next_cost = cost + 1 + heuristic(next_state, goal)
                heapq.heappush(queue, (next_cost, next_state))

start = np.array([[98, 30, 85, 44, 59, 40], [56, 68, 50, 61, 47, 15], [37, 48, 24, 81, 22, '_']])
goal = np.array([[98, 85, 68, 61, 59, 50], [48, 47, 44, 40, 37, 30], [24, 22, 15, '_', '_', '_']])
print(solve_puzzle(start, goal))
