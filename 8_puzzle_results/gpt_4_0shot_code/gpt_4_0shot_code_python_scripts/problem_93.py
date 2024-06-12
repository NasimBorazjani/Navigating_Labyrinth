
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

            if 0 <= x < puzzle.shape[0] and 0 <= y < puzzle.shape[1]:
                new_puzzle = np.copy(puzzle)
                new_puzzle[x-dx, y-dy], new_puzzle[x, y] = new_puzzle[x, y], new_puzzle[x-dx, y-dy]
                new_path = path + [new_puzzle[x-dx, y-dy]]
                new_h = heuristic(new_puzzle, goal)

                heapq.heappush(heap, (new_h + steps + 1, steps + 1, new_puzzle, new_path))

puzzle = np.array([[94, 87, 69, 81, 4, 79], ['_', 35, 86, 61, 57, 75], [41, 18, 65, 9, 53, 55]])
goal = np.array([[94, 87, 86, 81, 79, 75], [69, 65, 61, 57, 55, 53], [41, 35, 18, 9, 4, '_']])

print(solve(puzzle, goal))
