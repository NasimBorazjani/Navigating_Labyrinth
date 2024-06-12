
from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos):
    x, y = pos
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def solve_puzzle(initial_state):
    goal_state = [[81, 74, 72], [46, 45, 36], [10, 87, '_']]
    start = [(i, j) for i in range(3) for j in range(3) if initial_state[i][j] == '_'][0]
    goal = [(i, j) for i in range(3) for j in range(3) if goal_state[i][j] == '_'][0]
    queue = PriorityQueue()
    queue.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while not queue.empty():
        current = queue.get()[1]
        if current == goal:
            break
        for next in get_neighbors(current):
            x, y = next
            if 0 <= x < 3 and 0 <= y < 3:
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    queue.put((priority, next))
                    came_from[next] = current
    path = []
    current = goal
    while current != start:
        path.append(initial_state[current[0]][current[1]])
        current = came_from[current]
    path.reverse()
    return path

initial_state = [[10, 81, 46], [87, 74, 72], [36, 45, '_']]
print(solve_puzzle(initial_state))
