
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(current, rows, cols):
    i, j = current
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(i, j) for i, j in neighbors if 0 <= i < rows and 0 <= j < cols]

def a_star_search(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    queue = [(0, start)]
    visited = set()
    while queue:
        cost, current = heapq.heappop(queue)
        if current in visited:
            continue
        if current == goal:
            return cost
        visited.add(current)
        for neighbor in get_neighbors(current, rows, cols):
            if neighbor not in visited:
                priority = cost + heuristic(goal, neighbor)
                heapq.heappush(queue, (priority, neighbor))
    return -1

grid = [[89, 69, 35], [16, 14, 64], ['_', 23, 32]]
start = (2, 0)
goal = (0, 0)
print(a_star_search(start, goal, grid))
