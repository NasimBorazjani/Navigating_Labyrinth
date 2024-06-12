
import heapq
import copy

def heuristic(puzzle, goal):
    return sum(abs(b%4 - g%4) + abs(b//4 - g//4)
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
            x, y = current.index(0) % 4, current.index(0) // 4
            dx, dy = direction
            if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                neighbour = copy.deepcopy(current)
                i, j = x + dx, y + dy
                neighbour[y*4+x], neighbour[j*4+i] = neighbour[j*4+i], neighbour[y*4+x]
                if tuple(neighbour) not in seen:
                    seen[tuple(neighbour)] = current
                    heapq.heappush(queue, (heuristic(neighbour, goal), neighbour))

initial = [96, 53, 19, 15, 37, 32, 0, 87, 78, 100, 17, 13]
goal = [100, 96, 87, 78, 53, 37, 32, 19, 17, 15, 13, 0]
path = solve(initial, goal)
for i in range(1, len(path)):
    print("Move number", i, ":", path[i-1].index(0), "->", path[i].index(0))
