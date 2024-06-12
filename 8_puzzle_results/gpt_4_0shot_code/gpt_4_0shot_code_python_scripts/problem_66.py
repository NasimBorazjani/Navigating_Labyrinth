
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
            for i in range(len(current)):
                for j in range(len(current[0])):
                    if current[i][j] == '_':
                        x, y = i + direction[0], j + direction[1]
                        if 0 <= x < len(current) and 0 <= y < len(current[0]):
                            new_state = [row[:] for row in current]
                            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
                            new_cost = cost + 1 + heuristic(np.array(new_state), goal)
                            heapq.heappush(queue, (new_cost, new_state))
    return -1

start = [[94, 91, 33, 29, 78], [97, 20, 14, 54, 25], [38, 22, 32, 17, '_']]
goal = [[97, 94, 91, 78, 54], [33, 32, 29, 25, 22], [20, 17, 14, '_', '_']]
print(solve_puzzle(start, goal))
