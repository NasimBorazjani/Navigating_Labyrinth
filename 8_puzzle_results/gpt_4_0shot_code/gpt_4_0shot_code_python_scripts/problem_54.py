
import heapq

def heuristic(puzzle, goal):
    return sum(abs(b%4 - g%4) + abs(b//4 - g//4)
               for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 9)))

def astar(puzzle, goal):
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
        for neighbour in neighbours(current):
            if tuple(neighbour) not in seen:
                heapq.heappush(queue, (heuristic(neighbour, goal), neighbour))
                seen[tuple(neighbour)] = current

def neighbours(current):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current = current.index(0)
    for dx, dy in directions:
        x, y = current % 4 + dx, current // 4 + dy
        if 0 <= x < 4 and 0 <= y < 4:
            neighbour = current[:]
            neighbour[current], neighbour[x + y*4] = neighbour[x + y*4], neighbour[current]
            yield neighbour

puzzle = [100, '_', 99, 84, 59, 20, 56, 64, 74, 6, 57, 83]
goal = [100, 99, 84, 83, 74, 64, 59, 57, 56, 20, 6, '_']
print(astar(puzzle, goal))
