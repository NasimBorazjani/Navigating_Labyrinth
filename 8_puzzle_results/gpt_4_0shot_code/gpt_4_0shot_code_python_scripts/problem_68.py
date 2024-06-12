
import heapq

def heuristic(puzzle):
    """Calculate the Manhattan distance of the tiles from their goal positions."""
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != '_':
                goal_i, goal_j = divmod(14 - puzzle[i][j], 5)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def solve(puzzle):
    """Solve the puzzle using A* search."""
    start = [list(row) for row in puzzle]
    goal = [[92, 85, 78, 75, 74], [72, 70, 67, 66, 50], [48, 42, 32, 26, '_']]
    heap = [(heuristic(start), start)]
    visited = set()
    while heap:
        (h, puzzle) = heapq.heappop(heap)
        if puzzle == goal:
            return h
        visited.add(str(puzzle))
        i, j = next((i, j) for i, row in enumerate(puzzle) for j, cell in enumerate(row) if cell == '_')
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < 3 and 0 <= y < 5:
                new_puzzle = [list(row) for row in puzzle]
                new_puzzle[i][j], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[i][j]
                if str(new_puzzle) not in visited:
                    heapq.heappush(heap, (h + heuristic(new_puzzle) - heuristic(puzzle), new_puzzle))

puzzle = [[72, 92, '_', 78, 74], [70, 67, 85, 75, 66], [48, 42, 32, 26, 50]]
print(solve(puzzle))
