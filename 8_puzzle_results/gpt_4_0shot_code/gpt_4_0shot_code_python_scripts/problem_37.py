
import heapq
import copy

def heuristic(puzzle):
    return sum(abs(b % 4 - g % 4) + abs(b//4 - g//4)
               for b, g in ((puzzle.index(i), puzzle.index(i+1))
                            for i in range(1, 9)))

def search(puzzle):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    queue = [(heuristic(puzzle), puzzle)]
    seen = {tuple(puzzle): None}

    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = seen[tuple(current)]
            return path[::-1]
        for dx, dy in moves:
            x, y = current.index(0) % 4, current.index(0) // 4
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                new = copy.deepcopy(current)
                new[nx+ny*4], new[x+y*4] = new[x+y*4], new[nx+ny*4]
                if tuple(new) not in seen:
                    seen[tuple(new)] = current
                    heapq.heappush(queue, (heuristic(new) + len(path), new))

puzzle = [12, 78, 19, '_', 94, 66, 67, 49, 28, 83, 31, 47]
print(search(puzzle))
