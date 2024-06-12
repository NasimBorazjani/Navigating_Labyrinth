
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(current, rows, cols):
    i, j = current
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(i, j) for i, j in neighbors if 0 <= i < rows and 0 <= j < cols]

def a_star(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            break
        for neighbor in get_neighbors(current, rows, cols):
            new_cost = cost_so_far[current] + grid[neighbor[0]][neighbor[1]]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current
    path = []
    while current != start:
        path.append(grid[current[0]][current[1]])
        current = came_from[current]
    path.reverse()
    return path

grid = [[100, 96, 93, 82, 6, 19], [68, 53, 50, 9, 0, 24], [16, 15, 48, 10, 76, 74]]
start = (1, 4)
goal = (2, 5)
print(a_star(start, goal, grid))
