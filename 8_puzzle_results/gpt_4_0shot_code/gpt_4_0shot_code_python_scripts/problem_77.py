
import heapq
import copy

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] != '_':
                x, y = divmod(puzzle[i][j]-1, 5)
                distance += abs(x-i) + abs(y-j)
    return distance

def find_empty(puzzle):
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] == '_':
                return i, j

def astar(puzzle):
    start = puzzle
    heap = [(manhattan_distance(start), start)]
    while heap:
        cost, puzzle = heapq.heappop(heap)
        if manhattan_distance(puzzle) == 0:
            return puzzle
        i, j = find_empty(puzzle)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i+dx, j+dy
            if 0 <= x < 3 and 0 <= y < 5:
                new_puzzle = copy.deepcopy(puzzle)
                new_puzzle[i][j], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[i][j]
                heapq.heappush(heap, (cost+1+manhattan_distance(new_puzzle), new_puzzle))

puzzle = [[60, 66, 46, 8, 36], [81, '_', 88, 70, 24], [20, 17, 6, 62, 28]]
print(astar(puzzle))
