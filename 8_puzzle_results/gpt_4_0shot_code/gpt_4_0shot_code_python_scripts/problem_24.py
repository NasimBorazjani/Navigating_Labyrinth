
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), 0, puzzle, [])
    heap = [start]

    while heap:
        (h, steps, puzzle, path) = heapq.heappop(heap)

        if np.array_equal(puzzle, goal):
            return path

        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = np.where(puzzle == '_')
            x, y = x[0] + dx, y[0] + dy

            if 0 <= x < 3 and 0 <= y < 3:
                new_puzzle = np.copy(puzzle)
                new_puzzle[x-dx, y-dy], new_puzzle[x, y] = new_puzzle[x, y], new_puzzle[x-dx, y-dy]
                new_path = path + [new_puzzle[x-dx, y-dy]]
                heapq.heappush(heap, (heuristic(new_puzzle, goal) + steps + 1, steps + 1, new_puzzle, new_path))

puzzle = np.array([[35, 92, '_'], [32, 44, 94], [97, 75, 58]])
goal = np.array([[97, 94, 92], [75, 58, 44], [35, 32, '_']])
print(solve(puzzle, goal))
