
import heapq
import math


def a_star():
    # Define the initial state of the grid as a 2d tuple
    initial_state = ((0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1),
                      (0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1),
                      (0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1),
                      (1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1),
                      (1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1),
                      (1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0),
                      (0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0),
                      (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0),
                      (1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0),
                      (1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0),
                      (1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
                      (1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0),
                      (1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0),
                      (0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0))
    num_rows = 14
    num_cols = 14
    start = (0, 4)
    goal = (13, 12)

    visited_costs = {}
    visited_costs[start] = 0

    queue = [(0, 0, [start], start)]

    while queue:
        _, g, path, current = heapq.heappop(queue)

        if current == goal and len(path) == 18:
            return path

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row = current[0] + i
                new_col = current[1] + j
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] == 0:
                    new_pos = (new_row, new_col)
                    new_path = path + [new_pos]
                    new_cost = g + math.sqrt(i**2 + j**2)
                    if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                        visited_costs[new_pos] = new_cost
                        h = math.sqrt((new_row - goal[0])**2 + (new_col - goal[1])**2)
                        heapq.heappush(queue, (new_cost + h, new_cost, new_path, new_pos))

    return None


print(a_star())
