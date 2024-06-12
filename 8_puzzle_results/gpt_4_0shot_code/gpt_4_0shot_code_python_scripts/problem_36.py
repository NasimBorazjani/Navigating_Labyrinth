
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = puzzle
    heap = [(heuristic(start, goal), 0, start, [])]
    visited = set([start.tostring()])
    while heap:
        (h, steps, puzzle, path) = heapq.heappop(heap)
        if np.array_equal(puzzle, goal):
            return path
        for (d, new_puzzle) in moves(puzzle):
            if new_puzzle.tostring() not in visited:
                visited.add(new_puzzle.tostring())
                heapq.heappush(heap, (steps + 1 + heuristic(new_puzzle, goal), steps + 1, new_puzzle, path + [d]))

def moves(puzzle):
    directions = []
    i, j = np.where(puzzle == '_')
    if i > 0:
        new_puzzle = puzzle.copy()
        new_puzzle[i, j], new_puzzle[i - 1, j] = new_puzzle[i - 1, j], new_puzzle[i, j]
        directions.append((new_puzzle[i - 1, j], new_puzzle))
    if i < 2:
        new_puzzle = puzzle.copy()
        new_puzzle[i, j], new_puzzle[i + 1, j] = new_puzzle[i + 1, j], new_puzzle[i, j]
        directions.append((new_puzzle[i + 1, j], new_puzzle))
    if j > 0:
        new_puzzle = puzzle.copy()
        new_puzzle[i, j], new_puzzle[i, j - 1] = new_puzzle[i, j - 1], new_puzzle[i, j]
        directions.append((new_puzzle[i, j - 1], new_puzzle))
    if j < 3:
        new_puzzle = puzzle.copy()
        new_puzzle[i, j], new_puzzle[i, j + 1] = new_puzzle[i, j + 1], new_puzzle[i, j]
        directions.append((new_puzzle[i, j + 1], new_puzzle))
    return directions

start = np.array([[67, 86, 68, 29], [10, 95, '_', 44], [19, 80, 6, 50]])
goal = np.array([[95, 86, 80, 68], [67, 50, 44, 29], [19, 10, 6, '_']])
print(solve(start, goal))
