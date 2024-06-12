
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def a_star_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    districts_visited = set()

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal and len(districts_visited) == 3:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
                if next[0] <= 1:
                    districts_visited.add(1)
                elif 2 <= next[0] <= 6:
                    districts_visited.add(2)
                else:
                    districts_visited.add(3)

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Define the graph and the start and goal nodes here
# Then call a_star_search and reconstruct_path to get the path
