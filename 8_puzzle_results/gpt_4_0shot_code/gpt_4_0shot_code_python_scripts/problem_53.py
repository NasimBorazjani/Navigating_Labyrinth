
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
            if 0 <= nx < 3 and 0 <= ny < 4:
                neighbor = current.copy()
                neighbor[blank], neighbor[nx, ny] = neighbor[nx, ny], neighbor[blank]
                if str(neighbor.tolist()) not in visited:
                    heapq.heappush(queue, (cost + 1 + heuristic(neighbor, goal), neighbor))
    return -1

start = np.array([[38, 98, 84, 33], [63, 30, 61, 93], [73, 89, 85, '_']])
goal = np.array([[98, 93, 89, 85], [84, 73, 63, 38], [61, 33, 30, '_']])
print(solve_puzzle(start, goal))
