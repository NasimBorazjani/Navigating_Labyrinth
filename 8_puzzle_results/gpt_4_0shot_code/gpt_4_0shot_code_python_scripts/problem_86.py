
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

        for (d, new_puzzle) in moves(puzzle):
            if new_puzzle is not None and not any(np.array_equal(p, new_puzzle) for (_, _, _, p) in heap):
                heapq.heappush(heap, (steps + 1 + heuristic(new_puzzle, goal), steps + 1, new_puzzle, path + [d]))

def moves(puzzle):
    directions = []
    i, j = np.where(puzzle == '_')
    i, j = int(i), int(j)

    if i > 0:
        new_puzzle = np.copy(puzzle)
        new_puzzle[i][j], new_puzzle[i - 1][j] = new_puzzle[i - 1][j], new_puzzle[i][j]
        directions.append((new_puzzle[i - 1][j], new_puzzle))
    if i < 2:
        new_puzzle = np.copy(puzzle)
        new_puzzle[i][j], new_puzzle[i + 1][j] = new_puzzle[i + 1][j], new_puzzle[i][j]
        directions.append((new_puzzle[i + 1][j], new_puzzle))
    if j > 0:
        new_puzzle = np.copy(puzzle)
        new_puzzle[i][j], new_puzzle[i][j - 1] = new_puzzle[i][j - 1], new_puzzle[i][j]
        directions.append((new_puzzle[i][j - 1], new_puzzle))
    if j < 4:
        new_puzzle = np.copy(puzzle)
        new_puzzle[i][j], new_puzzle[i][j + 1] = new_puzzle[i][j + 1], new_puzzle[i][j]
        directions.append((new_puzzle[i][j + 1], new_puzzle))

    return directions

puzzle = np.array([[88, 71, 83, 72, 37], [98, 43, 53, '_', 82], [24, 20, 54, 14, 21]])
goal = np.array([[98, 88, 83, 82, 72], [71, 54, 53, 43, 37], [24, 21, 20, 14, '_']])

print(solve(puzzle, goal))
