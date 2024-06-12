
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), puzzle, [])
    heap = [start]

    while heap:
        (h, puzzle, path) = heapq.heappop(heap)

        if np.array_equal(puzzle, goal):
            return path

        empty_spot = tuple(np.argwhere(puzzle == '_')[0])
        for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_spot = (empty_spot[0] + direction[0], empty_spot[1] + direction[1])
            if 0 <= new_spot[0] < puzzle.shape[0] and 0 <= new_spot[1] < puzzle.shape[1]:
                new_puzzle = puzzle.copy()
                new_puzzle[empty_spot], new_puzzle[new_spot] = new_puzzle[new_spot], new_puzzle[empty_spot]
                new_h = heuristic(new_puzzle, goal)
                heapq.heappush(heap, (new_h, new_puzzle, path + [new_puzzle[new_spot]]))

puzzle = np.array([[95, '_', 80, 18], [67, 66, 35, 94], [27, 26, 69, 53]])
goal = np.array([[95, 94, 80, 69], [67, 66, 53, 35], [27, 26, 18, '_']])
print(solve(puzzle, goal))
