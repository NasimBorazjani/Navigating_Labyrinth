
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = puzzle
    pr_queue = []
    heapq.heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    visited = set()
    while pr_queue:
        _, g, path, current = heapq.heappop(pr_queue)
        if np.array_equal(current, goal):
            return path
        visited.add(str(current.reshape(-1)))
        r, c = np.where(current == '_')
        r, c = r[0], c[0]
        for dr, dc, move in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < current.shape[0] and 0 <= nc < current.shape[1]:
                next_state = current.copy()
                next_state[r, c], next_state[nr, nc] = next_state[nr, nc], next_state[r, c]
                if str(next_state.reshape(-1)) not in visited:
                    heapq.heappush(pr_queue, (g + 1 + heuristic(next_state, goal), g + 1, path + str(next_state[nr, nc]) + ",", next_state))
    return "No solution"

start = np.array([[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']])
goal = np.array([[93, 92, 91, 83, 79, 74], [72, 67, 65, 63, 62, 58], [41, 34, 29, 27, 24, '_']])
print(solve(start, goal))
