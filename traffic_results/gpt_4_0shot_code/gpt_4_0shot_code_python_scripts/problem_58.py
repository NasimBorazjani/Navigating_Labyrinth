
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def a_star_search(graph, start, goal, districts):
    frontier = PriorityQueue()
    frontier.put((0, [start]))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    visited_districts = {start: districts[start[0]]}

    while not frontier.empty():
        _, path = frontier.get()
        current = path[-1]

        if current == goal:
            return path

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                new_path = path + [next]
                frontier.put((priority, new_path))
                came_from[next] = current
                visited_districts[next] = districts[next[0]]

        if len(set(visited_districts.values())) < 3:
            continue

    return None

# Define the city map, start and end points, and districts here
# Then call a_star_search(city_map, start, end, districts)
