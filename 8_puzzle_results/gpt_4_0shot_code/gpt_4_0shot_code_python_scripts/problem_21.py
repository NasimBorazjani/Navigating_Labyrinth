
import heapq
import numpy as np

def manhattan_distance(puzzle):
    goal = [[94, 71, 61], [58, 53, 50], [25, 18, '_']]
    return sum(abs(b%3 - g%3) + abs(b//3 - g//3)
               for b, val in np.ndenumerate(puzzle)
               for g, goal_val in np.ndenumerate(goal)
               if val == goal_val)

def solve_puzzle(puzzle):
    start = puzzle
    heap = [(manhattan_distance(start), start)]
    visited = set()
    moves = {str(start): []}

    while heap:
        (h, puzzle) = heapq.heappop(heap)
        if puzzle == [[94, 71, 61], [58, 53, 50], [25, 18, '_']]:
            return moves[str(puzzle)]
        visited.add(str(puzzle))
        blank = tuple(i for i in range(9) if puzzle[i//3][i%3] == '_')[0]
        for d in (-1, 1, -3, 3):
            neighbor = blank + d
            if 0 <= neighbor < 9 and not (blank % 3 == 2 and d == 1) and not (blank % 3 == 0 and d == -1):
                new_puzzle = [row[:] for row in puzzle]
                new_puzzle[blank//3][blank%3], new_puzzle[neighbor//3][neighbor%3] = new_puzzle[neighbor//3][neighbor%3], new_puzzle[blank//3][blank%3]
                if str(new_puzzle) not in visited:
                    heapq.heappush(heap, (h - manhattan_distance(puzzle) + manhattan_distance(new_puzzle), new_puzzle))
                    moves[str(new_puzzle)] = moves[str(puzzle)] + [new_puzzle[neighbor//3][neighbor%3]]

puzzle = [[25, 71, 58], [61, 94, 53], [50, 18, '_']]
print(solve_puzzle(puzzle))
