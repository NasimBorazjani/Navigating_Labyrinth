
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_neighbors(position, puzzle):
    x, y = position
    neighbors = []
    if x > 0:
        neighbors.append(((x - 1, y), puzzle[x - 1][y]))
    if x < 2:
        neighbors.append(((x + 1, y), puzzle[x + 1][y]))
    if y > 0:
        neighbors.append(((x, y - 1), puzzle[x][y - 1]))
    if y < 3:
        neighbors.append(((x, y + 1), puzzle[x][y + 1]))
    return neighbors

def solve_puzzle(puzzle):
    start = None
    goal = (2, 3)
    for i in range(3):
        for j in range(4):
            if puzzle[i][j] == '_':
                start = (i, j)
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while frontier:
        current = heapq.heappop(frontier)[1]
        if current == goal:
            break
        for next in get_neighbors(current, puzzle):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
    current = goal
    path = []
    while current != start:
        path.append(puzzle[current[0]][current[1]])
        current = came_from[current]
    path.reverse()
    return path

puzzle = [[10, 96, 60, '_'], [98, 73, 14, 58], [53, 3, 21, 67]]
print(solve_puzzle(puzzle))
