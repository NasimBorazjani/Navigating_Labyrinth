
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    districts_visited = {1: False, 2: False, 3: False}
    if start[0] <= 4:
        districts_visited[1] = True
    elif start[0] <= 9:
        districts_visited[2] = True
    else:
        districts_visited[3] = True

    while not frontier.empty():
        current = frontier.get()

        if current == goal and all(districts_visited.values()):
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                if next[0] <= 4:
                    districts_visited[1] = True
                elif next[0] <= 9:
                    districts_visited[2] = True
                else:
                    districts_visited[3] = True

    return came_from, cost_so_far

# Define the graph, start, and goal here
graph = Graph(city_map)
start = (10, 12)
goal = (4, 3)

came_from, cost_so_far = a_star_search(graph, start, goal)
path = reconstruct_path(came_from, start, goal)
