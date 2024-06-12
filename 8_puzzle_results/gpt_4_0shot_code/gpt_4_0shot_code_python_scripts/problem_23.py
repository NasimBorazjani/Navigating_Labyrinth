
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return np.sum(puzzle != goal)

def solve(puzzle, goal):
    start = puzzle.index('_')
    frontier = [(heuristic(puzzle, goal), puzzle, start, [])]
    explored = set()
    while frontier:
        _, current, current_index, moves = heapq.heappop(frontier)
        if current == goal:
            return moves
        explored.add(tuple(current))
        for direction in [-1, 1, -3, 3]:
            neighbor_index = current_index + direction
            if (0 <= neighbor_index < 9 and
                not (current_index % 3 == 2 and direction == 1) and
                not (current_index % 3 == 0 and direction == -1)):
                neighbor = current[:]
                neighbor[current_index], neighbor[neighbor_index] = neighbor[neighbor_index], neighbor[current_index]
                if tuple(neighbor) not in explored:
                    heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor, neighbor_index, moves + [neighbor[neighbor_index]]))
    return None

initial = [62, 43, 28, 59, 34, 53, 29, 76, '_']
goal = [76, 62, 59, 53, 43, 34, 29, 28, '_']
print(solve(initial, goal))
