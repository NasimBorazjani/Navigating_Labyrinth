
import heapq

def heuristic(puzzle, goal):
    return sum(abs(b%4 - g%4) + abs(b//4 - g//4)
               for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 9)))

def search(puzzle, goal):
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
            x, y = index % 4, index // 4
            dx, dy = direction
            if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                neighbour[index], neighbour[index + dy * 4 + dx] = neighbour[index + dy * 4 + dx], neighbour[index]
                if tuple(neighbour) not in seen:
                    seen[tuple(neighbour)] = current
                    heapq.heappush(queue, (heuristic(neighbour, goal), neighbour))

puzzle = [61, '_', 99, 70, 42, 81, 90, 16, 41, 54, 28, 45]
goal = [99, 90, 81, 70, 61, 54, 45, 42, 41, 28, 16, '_']
path = search(puzzle, goal)
for i in path:
    print(i)
