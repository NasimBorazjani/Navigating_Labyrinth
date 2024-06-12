
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = puzzle.copy()
    heap = [(heuristic(start, goal), 0, start, [])]
    visited = set([str(start)])

    while heap:
        (h, steps, puzzle, path) = heapq.heappop(heap)

        if np.array_equal(puzzle, goal):
            return path

        empty = tuple(map(int, np.where(puzzle == '_')))
        for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_empty = tuple(map(sum, zip(empty, direction)))
            if 0 <= new_empty[0] < puzzle.shape[0] and 0 <= new_empty[1] < puzzle.shape[1]:
                new_puzzle = puzzle.copy()
                new_puzzle[empty], new_puzzle[new_empty] = new_puzzle[new_empty], new_puzzle[empty]
                if str(new_puzzle) not in visited:
                    visited.add(str(new_puzzle))
                    heapq.heappush(heap, (heuristic(new_puzzle, goal) + steps + 1, steps + 1, new_puzzle, path + [new_puzzle[empty]]))

    return []

puzzle = np.array([[69, 56, 8, 67], [15, 47, 44, 30], [73, '_', 24, 63]])
goal = np.array([[73, 69, 67, 63], [56, 47, 44, 30], [24, 15, 8, '_']])
print(solve(puzzle, goal))
