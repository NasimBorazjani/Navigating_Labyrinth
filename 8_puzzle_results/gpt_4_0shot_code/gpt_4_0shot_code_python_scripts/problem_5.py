
import heapq
import copy

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != '_':
                x, y = divmod(puzzle[i][j]-1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def solve(puzzle):
    start = [puzzle, 'start', 0, manhattan_distance(puzzle)]
    heap = []
    heapq.heappush(heap, start)

    while heap:
        current = heapq.heappop(heap)
        if current[0] == [[98, 95, 89], [78, 70, 58], [38, 7, '_']]:
            moves = []
            while current[1] != 'start':
                moves.insert(0, current[1])
                current = current[2]
            return moves

        blank = [(index, row.index('_')) for index, row in enumerate(current[0]) if '_' in row][0]
        for swap in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i = blank[0] + swap[0]
            j = blank[1] + swap[1]
            if 0 <= i < 3 and 0 <= j < 3:
                temp = copy.deepcopy(current[0])
                temp[blank[0]][blank[1]], temp[i][j] = temp[i][j], temp[blank[0]][blank[1]]
                heapq.heappush(heap, [temp, temp[i][j], current, current[3] + 1 + manhattan_distance(temp) - manhattan_distance(current[0])])

print(solve([[78, 98, 89], [38, '_', 7], [58, 95, 70]]))
