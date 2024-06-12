
import heapq

def heuristic(puzzle, target):
    return sum(abs(b%3 - g%3) + abs(b//3 - g//3)
               for b, g in ((puzzle.index(i), target.index(i)) for i in range(1, 9)))

def solve(puzzle, target):
    queue = [(heuristic(puzzle, target), puzzle)]
    seen = {tuple(puzzle): None}

    while queue:
        _, current = heapq.heappop(queue)
        if current == target:
            path = []
            while current:
                path.append(current)
                current = seen[tuple(current)]
            return path[::-1]
        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = current.index(0) % 3, current.index(0) // 3
            dx, dy = direction
            if 0 <= x + dx < 3 and 0 <= y + dy < 3:
                swap = current.index(0) + dx + dy * 3
                new_puzzle = current[:]
                new_puzzle[current.index(0)], new_puzzle[swap] = new_puzzle[swap], new_puzzle[current.index(0)]
                if tuple(new_puzzle) not in seen:
                    seen[tuple(new_puzzle)] = current
                    heapq.heappush(queue, (heuristic(new_puzzle, target) + len(path), new_puzzle))

initial = [66, 35, 51, 76, 0, 73, 90, 54, 22]
target = [90, 76, 73, 66, 54, 51, 35, 22, 0]
solution = solve(initial, target)
for s in solution:
    print(s)
