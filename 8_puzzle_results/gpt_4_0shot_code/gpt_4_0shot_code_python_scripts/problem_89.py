
import heapq

def heuristic(puzzle, goal):
    return sum(abs(b%5 - g%5) + abs(b//5 - g//5)
               for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 16)))

def search(puzzle, goal):
    queue = [(heuristic(puzzle, goal), puzzle)]
    seen = {tuple(puzzle): None}
    while queue:
        _, puzzle = heapq.heappop(queue)
        if puzzle == goal:
            path = []
            while puzzle:
                path.append(puzzle)
                puzzle = seen[tuple(puzzle)]
            return path[::-1]
        for d in (-1, 1, -5, 5):
            neighbor = puzzle.index(0) + d
            if 0 <= neighbor < len(puzzle):
                if abs(puzzle.index(0)%5 - neighbor%5) + abs(puzzle.index(0)//5 - neighbor//5) == 1:
                    puzzle[neighbor], puzzle[puzzle.index(0)] = puzzle[puzzle.index(0)], puzzle[neighbor]
                    if tuple(puzzle) not in seen:
                        seen[tuple(puzzle)] = puzzle[:]
                        heapq.heappush(queue, (heuristic(puzzle, goal), puzzle[:]))
                    puzzle[neighbor], puzzle[puzzle.index(0)] = puzzle[puzzle.index(0)], puzzle[neighbor]

puzzle = [71, 36, 63, 32, 15, 20, 21, 65, 0, 54, 45, 96, 29, 31, 55]
goal = sorted(puzzle, reverse=True)
goal[-1] = 0
path = search(puzzle, goal)
for i in range(1, len(path)):
    print(path[i-1].index(0), '->', path[i].index(0))
