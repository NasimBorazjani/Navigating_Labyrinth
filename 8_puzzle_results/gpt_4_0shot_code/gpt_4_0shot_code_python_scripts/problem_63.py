
import heapq

def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] != '_':
                x, y = divmod(puzzle[i][j]-1, 5)
                distance += abs(x-i) + abs(y-j)
    return distance

def swap(puzzle, empty, target):
    new_puzzle = [row[:] for row in puzzle]
    new_puzzle[empty[0]][empty[1]], new_puzzle[target[0]][target[1]] = new_puzzle[target[0]][target[1]], new_puzzle[empty[0]][empty[1]]
    return new_puzzle

def solve(puzzle):
    goal = [[i*5+j for j in range(5, 0, -1)] for i in range(2, -1, -1)]
    goal[2][4] = '_'
    queue = [(manhattan_distance(puzzle), puzzle, [], None)]
    visited = set([str(puzzle)])

    while queue:
        _, puzzle, path, empty = heapq.heappop(queue)
        if puzzle == goal:
            return path
        if empty is None:
            empty = next((i, j) for i in range(3) for j in range(5) if puzzle[i][j] == '_')
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = empty[0]+dx, empty[1]+dy
            if 0 <= x < 3 and 0 <= y < 5:
                new_puzzle = swap(puzzle, empty, (x, y))
                if str(new_puzzle) not in visited:
                    heapq.heappush(queue, (manhattan_distance(new_puzzle)+len(path)+1, new_puzzle, path+[puzzle[x][y]], (x, y)))
                    visited.add(str(new_puzzle))

puzzle = [[98, 80, 41, 91, 88], [75, 93, 24, '_', 12], [38, 37, 49, 65, 43]]
print(solve(puzzle))
