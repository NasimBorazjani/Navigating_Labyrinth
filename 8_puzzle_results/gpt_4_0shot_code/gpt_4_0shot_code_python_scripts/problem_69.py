
import heapq
import numpy as np

def heuristic(puzzle, goal):
    return sum(abs(b%5 - g%5) + abs(b//5 - g//5)
               for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 16)))

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
            neighbour = current[:]
            index = neighbour.index(0)
            x, y = index % 5, index // 5
            dx, dy = direction
            if 0 <= x + dx < 5 and 0 <= y + dy < 3:
                neighbour[index], neighbour[index + dy * 5 + dx] = neighbour[index + dy * 5 + dx], neighbour[index]
                if tuple(neighbour) not in seen:
                    seen[tuple(neighbour)] = current
                    heapq.heappush(queue, (heuristic(neighbour, goal), neighbour))

initial = [0, 83, 11, 57, 59, 89, 61, 99, 76, 63, 42, 35, 25, 48, 54]
goal = [99, 89, 83, 76, 63, 61, 59, 57, 54, 48, 42, 35, 25, 11, 0]
path = solve(initial, goal)

for i in range(1, len(path)):
    print(np.array(path[i]).reshape(3, 5))
