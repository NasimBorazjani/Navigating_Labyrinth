
import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(current, rows, cols):
    i, j = current
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(i, j) for i, j in neighbors if 0 <= i < rows and 0 <= j < cols]

def a_star_search(start, goal, graph):
    rows, cols = len(graph), len(graph[0])
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        for next in get_neighbors(current, rows, cols):
            new_cost = cost_so_far[current] + graph[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
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

graph = [[52, 0, 99, 42], [56, 67, 49, 68], [88, 23, 33, 26]]
start, goal = (0, 1), (2, 3)
came_from, cost_so_far = a_star_search(start, goal, graph)
path = reconstruct_path(came_from, start, goal)
print([graph[i][j] for i, j in path])
