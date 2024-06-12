
import heapq
import numpy as np

def manhattan_distance(puzzle):
    goal = [[91, 71, 58, 56, 51], [46, 45, 43, 33, 24], [21, 17, 14, 13, '_']]
    distance = 0
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] != '_':
                for x in range(3):
                    for y in range(5):
                        if goal[x][y] == puzzle[i][j]:
                            distance += abs(x - i) + abs(y - j)
    return distance

def solve_puzzle(puzzle):
    goal = [[91, 71, 58, 56, 51], [46, 45, 43, 33, 24], [21, 17, 14, 13, '_']]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(manhattan_distance(puzzle), puzzle, [])]
    visited = set()

    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current == goal:
            return path
        visited.add(str(current))
        empty = [(index, row.index('_')) for index, row in enumerate(current) if '_' in row][0]
        for move in moves:
            x, y = empty[0] + move[0], empty[1] + move[1]
            if 0 <= x < 3 and 0 <= y < 5:
                new_puzzle = [row.copy() for row in current]
                new_puzzle[empty[0]][empty[1]], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[empty[0]][empty[1]]
                if str(new_puzzle) not in visited:
                    heapq.heappush(heap, (cost - manhattan_distance(current) + manhattan_distance(new_puzzle) + 1, new_puzzle, path + [new_puzzle[x][y]]))

puzzle = [[58, 51, 56, 43, 33], [91, 71, 21, 14, 24], [46, 45, '_', 17, 13]]
print(solve_puzzle(puzzle))
