
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1),
                      (1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0),
                      (0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
                      (0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0),
                      (1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0),
                      (1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
                      (0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0),
                      (0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                      (0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1),
                      (1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0),
                      (1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1),
                      (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1))
    num_rows = 12
    num_cols = 12
    start = (1, 11)
    goal = (11, 3)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == goal and len(path) == 9:
            return path

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and 0 <= current[0] + i < num_rows and 0 <= current[1] + j < num_cols:
                    new_pos = (current[0] + i, current[1] + j)
                    if initial_state[new_pos[0]][new_pos[1]] == 0 and new_pos not in path:
                        new_path = path + [new_pos]
                        new_cost = g + math.sqrt(i**2 + j**2)
                        if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                            visited_costs[new_pos] = new_cost
                            heapq.heappush(queue, (new_cost + math.sqrt((new_pos[0] - goal[0])**2 + (new_pos[1] - goal[1])**2), new_cost, new_path, new_pos))

    return None


print(a_star())
