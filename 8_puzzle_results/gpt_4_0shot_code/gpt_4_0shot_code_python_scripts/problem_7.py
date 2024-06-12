
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
        visited.add(str(current.tolist()))
        blank = tuple(map(int, np.where(current == '_')))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = blank[0] + dx, blank[1] + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor = current.copy()
                neighbor[blank], neighbor[nx, ny] = neighbor[nx, ny], neighbor[blank]
                if str(neighbor.tolist()) not in visited:
                    heapq.heappush(queue, (cost + 1 + heuristic(neighbor, goal), neighbor))
    return -1

start = np.array([[36, 16, 48], [86, '_', 13], [89, 31, 37]])
goal = np.array([[89, 86, 48], [36, 31, 16], [13, 37, '_']])
print(solve_puzzle(start, goal))
