
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), 0, puzzle, [], None)
    heap = [start]
    while heap:
        (h, g, puzzle, path, prev_move) = heapq.heappop(heap)
        if np.array_equal(puzzle, goal):
            return path
        moves = [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]
        for dx, dy, move in moves:
            if move == prev_move:
                continue
            empty = np.argwhere(puzzle == '_')[0]
            swap = empty + [dx, dy]
            if 0 <= swap[0] < puzzle.shape[0] and 0 <= swap[1] < puzzle.shape[1]:
                new_puzzle = puzzle.copy()
                new_puzzle[empty[0]][empty[1]], new_puzzle[swap[0]][swap[1]] = new_puzzle[swap[0]][swap[1]], new_puzzle[empty[0]][empty[1]]
                new_h = heuristic(new_puzzle, goal)
                heapq.heappush(heap, (new_h + g + 1, g + 1, new_puzzle, path + [new_puzzle[swap[0]][swap[1]]], move))

puzzle = np.array([[93, 26, 39, 51, 69], [27, '_', 43, 7, 89], [63, 91, 23, 68, 17]])
goal = np.array([[93, 91, 89, 69, 68], [63, 51, 43, 39, 27], [26, 23, 17, '_', '_']])
print(solve(puzzle, goal))
