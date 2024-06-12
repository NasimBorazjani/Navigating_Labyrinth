
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_district(pos):
    if 0 <= pos[0] <= 4:
        return 1
    elif 5 <= pos[0] <= 8:
        return 2
    else:
        return 3

def a_star_search(city_map, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start, {get_district(start)}))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current, districts = frontier.get()

        if current == goal and len(districts) == 3:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next = (current[0] + dx, current[1] + dy)
            if (0 <= next[0] < len(city_map) and 0 <= next[1] < len(city_map[0]) and
                city_map[next[0]][next[1]] != 'x'):
                new_cost = cost_so_far[current] + city_map[next[0]][next[1]]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    new_districts = districts | {get_district(next)}
                    frontier.put((priority, next, new_districts))
                    came_from[next] = current

    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

city_map = [
    ['x', 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, 'x', 3, 'x'],
    ['x', 11, 'x', 'x', 'x', 12, 'x', 19, 15, 4, 'x', 'x', 'x', 'x', 'x'],
    [4, 1, 'x', 8, 'x', 12, 17, 'x', 14, 4, 9, 11, 13, 6, 19],
    [2, 'x', 6, 14, 15, 'x', 18, 9, 'x', 10, 10, 'x', 'x', 1, 'x'],
    ['x', 11, 'x', 8, 'x', 5, 'x', 8, 7, 6, 'x', 'x', 13, 6, 'x'],
    ['x', 'x', 'x', 17, 'x', 13, 'x', 'x', 'x', 'x', 18, 19, 5, 'x', 'x'],
    ['x', 12, 18, 'x', 'x', 'x', 19, 'x', 12, 'x', 11, 7, 19, 12, 'x'],
    [6, 6, 'x', 6, 4, 'x', 18, 'x', 'x', 15, 18, 'x', 6, 8, 'x'],
    [10, 10, 'x', 'x', 6, 4, 11, 19, 'x', 9, 'x', 2, 'x', 3, 14],
    ['x', 18, 14, 10, 'x', 1, 'x', 6, 'x', 15, 'x', 6, 'x', 14, 'x'],
    ['x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x', 'x'],
    [12, 'x', 6, 'x', 8, 5, 6, 6, 8, 'x', 'x', 'x', 'x', 4, 7],
    ['x', 'x', 1, 8, 10, 4, 10, 17, 19, 11, 2, 'x', 'x', 'x', 16],
    ['x', 'x', 'x', 17, 8, 19, 'x', 14, 'x', 17, 17, 5, 7, 6, 7],
    [1, 'x', 14, 'x', 3, 'x', 18, 6, 18, 8, 'x', 13, 10, 'x', 'x']
]

start = (7, 0)
goal = (4, 13)
print(a_star_search(city_map, start, goal))
