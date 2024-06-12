
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(current, rows, cols):
    i, j = current
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(i, j) for i, j in neighbors if 0 <= i < rows and 0 <= j < cols]

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = [(0, start, [])]
    seen = set()
    while queue:
        cost, current, path = heapq.heappop(queue)
        if current == goal:
            return path + [grid[current[0]][current[1]]]
        if current in seen:
            continue
        seen.add(current)
        for neighbor in get_neighbors(current, rows, cols):
            if neighbor not in seen:
                priority = cost + heuristic(goal, neighbor)
                heapq.heappush(queue, (priority, neighbor, path + [grid[current[0]][current[1]]]))
    return []

grid = [[79, 98, 87, 83], [56, 76, 65, 91], [25, None, 36, 70]]
start = (2, 1)
goal = (2, 3)
print(a_star_search(grid, start, goal))
