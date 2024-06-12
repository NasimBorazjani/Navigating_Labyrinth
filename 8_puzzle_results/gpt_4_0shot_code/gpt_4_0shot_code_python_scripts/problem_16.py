
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(np.abs(puzzle - goal))

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), 0, '', puzzle, None)
    heap = [start]

    while heap:
        (h, g, path, puzzle, prev) = heapq.heappop(heap)

        if np.array_equal(puzzle, goal):
            return path

        moves = np.array([[0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U'], [1, 0, 'D']])
        pos = np.argwhere(puzzle == '_')[0]

        for dx, dy, direction in moves:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < 3 and 0 <= y < 3 and (prev is None or not np.array_equal(prev, puzzle)):
                new_puzzle = np.copy(puzzle)
                new_puzzle[pos[0], pos[1]], new_puzzle[x, y] = new_puzzle[x, y], new_puzzle[pos[0], pos[1]]
                heapq.heappush(heap, (g + heuristic(new_puzzle, goal), g + 1, path + direction, new_puzzle, puzzle))

puzzle = np.array([[77, 81, 74], [93, 85, 98], [59, 53, '_']])
goal = np.array([[98, 93, 85], [81, 77, 74], [59, 53, '_']])

print(solve(puzzle, goal))
