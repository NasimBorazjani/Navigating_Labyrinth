
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = (heuristic(puzzle, goal), 0, puzzle, None, None)
    heap = [start]
    visited = set()
    while heap:
        (_, g, puzzle, prev, move) = heapq.heappop(heap)
        if np.array_equal(puzzle, goal):
            moves = []
            while move is not None:
                moves.append(move)
                _, _, _, _, move = prev
            return moves[::-1]
        visited.add(str(puzzle))
        y, x = np.where(puzzle == '_')
        for dy, dx, move in [(-1, 0, puzzle[y-1, x]), (1, 0, puzzle[y+1, x]), (0, -1, puzzle[y, x-1]), (0, 1, puzzle[y, x+1])]:
            if 0 <= y+dy < puzzle.shape[0] and 0 <= x+dx < puzzle.shape[1] and str(puzzle) not in visited:
                next_puzzle = puzzle.copy()
                next_puzzle[y, x], next_puzzle[y+dy, x+dx] = next_puzzle[y+dy, x+dx], next_puzzle[y, x]
                heapq.heappush(heap, (g + 1 + heuristic(next_puzzle, goal), g + 1, next_puzzle, (heuristic(puzzle, goal), g, puzzle, prev, move), move))

puzzle = np.array([[91, 86, 16, 48, 81], [13, 89, 5, '_', 58], [54, 22, 36, 37, 31]])
goal = np.array([[91, 89, 86, 81, 58], [54, 48, 37, 36, 31], [22, 16, 13, 5, '_']])
print(solve(puzzle, goal))
