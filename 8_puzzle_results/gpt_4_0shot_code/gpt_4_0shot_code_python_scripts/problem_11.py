
import heapq

def heuristic(puzzle, goal):
    return sum(abs(b%3 - g%3) + abs(b//3 - g//3)
               for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 9)))

def solve(puzzle, goal):
    queue = [(heuristic(puzzle, goal), puzzle)]
    seen = {tuple(puzzle): None}

    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = seen[tuple(current)]
            return path[::-1]
        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            adjacent = current.index(0)
            x, y = adjacent % 3, adjacent // 3
            dx, dy = direction
            if 0 <= x + dx < 3 and 0 <= y + dy < 3:
                swap = y * 3 + x
                swap_with = (y + dy) * 3 + (x + dx)
                copy = list(current)
                copy[swap], copy[swap_with] = copy[swap_with], copy[swap]
                if tuple(copy) not in seen:
                    seen[tuple(copy)] = current
                    heapq.heappush(queue, (heuristic(copy, goal), copy))

puzzle = [59, 76, 55, 54, 0, 85, 50, 95, 53]
goal = [95, 85, 76, 59, 55, 54, 53, 50, 0]
print(solve(puzzle, goal))
