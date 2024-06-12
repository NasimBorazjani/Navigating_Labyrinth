
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
    districts_visited = set()

    while not frontier.empty():
        current = frontier.get()

        if current == goal and len(districts_visited) == 3:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                if next[0] < 5:
                    districts_visited.add(1)
                elif next[0] < 9:
                    districts_visited.add(2)
                else:
                    districts_visited.add(3)

    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Define the graph and the start and goal nodes here
graph = Graph(city_map)
start = (7, 2)
goal = (4, 14)

path = a_star_search(graph, start, goal)
print(path)
