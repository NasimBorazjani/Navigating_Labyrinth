
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), 0, '', puzzle)
    heap = [start]

    while heap:
        (est, steps, path, puzzle) = heapq.heappop(heap)

        if np.array_equal(puzzle, goal):
            return path

        i, j = np.where(puzzle == '_')
        i, j = int(i), int(j)

        for (di, dj, move) in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            if 0 <= i + di < puzzle.shape[0] and 0 <= j + dj < puzzle.shape[1]:
                new_puzzle = np.copy(puzzle)
                new_puzzle[i, j], new_puzzle[i + di, j + dj] = new_puzzle[i + di, j + dj], new_puzzle[i, j]
                new_est = steps + 1 + heuristic(new_puzzle, goal)

                heapq.heappush(heap, (new_est, steps + 1, path + str(new_puzzle[i + di, j + dj]) + ',', new_puzzle))

    return "No solution found"

puzzle = np.array([[92, 79, 74, 46, 64, 44], [39, 59, 75, 26, 47, 73], [29, 53, 56, '_', 16, 17]])
goal = np.array([[92, 79, 74, 64, 59, 56], [46, 44, 39, 47, 29, 26], [75, 73, 53, 17, 16, '_']])

print(solve(puzzle, goal))
